from BeautifulSoup import BeautifulSoup
import re
import argparse
from util.words import STATES, COUNTRIES, CORPS, PLACES, BASE_URL, EXHIBIT21_WORDS, JUNK, EXCLUDE_CORPS
from models.models import Company
from downloader import Downloader
from util.cleaner import clean_name, clean_addr, first_letter_caps


class Parser(object):

    def __init__(self, cache_path, backend):
        self.downloader = Downloader(cache_path)
        self.backend = backend

    def parse(self, years, quarters):

        #Get the urls of the 10K forms,
        form_10k_urls = self.get_10k_urls(years = years, quarters = quarters)
        self.get_10k_docs(form_10k_urls)

    def get_10k_urls(self, years = [2012], quarters = [1]):
        urls = []
        for year in years:
            for qtr in quarters:
                lines = self.downloader.get_idx(year, qtr)
                k_lines = [line for line in lines if '10-K' in line]
                for line in k_lines:
                    url = re.search('[\S]*\.txt', line)
                    urls.append(url.group(0))
        return urls
                

    def get_10k_docs(self, urls):
        """
        Steps:
        Get the 10K documents for a list of URLs in the index file
        Find the company name and addresses in the 10k filing
        Look for an exhibit 21 document within the 10k
        If the exhibit 21 exists, get that, then pull the subsidiaries out and add them
            to the newly created company


        """
        companies = []
        for url in urls:
            company = Company()
            full = BASE_URL + '/Archives/%s-index.htm' % url[0:len(url)-4]
            company.url = full
            contents = self.downloader.get_url(full)

            try:
                soup = BeautifulSoup(contents, convertEntities=BeautifulSoup.HTML_ENTITIES)
                company_name = soup.findAll('span', attrs={'class' : 'companyName'})
                company_name = re.search('(?<=>).*?(?=<)', str(company_name[0]), re.DOTALL).group(0)
            except IndexError:
                self.downloader.purge(full)
                contents = self.downloader.get_url(full)
                soup = BeautifulSoup(contents, convertEntities=BeautifulSoup.HTML_ENTITIES)
                company_name = soup.findAll('span', attrs={'class' : 'companyName'})
                company_name = re.search('(?<=>).*?(?=<)', str(company_name[0]), re.DOTALL).group(0)

            company.name = clean_name(company_name)

            existing = self.backend.get_company(company.name)
            if not existing:
                addresses = soup.findAll('div', attrs={'class' : 'mailer'})
                for address in addresses:
                    if "business address" in address.text.lower():
                        #This is the business address
                        company.business_address = clean_addr(self.extract_address(address))
                        pass
                    if "mailing address" in address.text.lower():
                        company.mailing_address =  clean_addr(self.extract_address(address))

                table_rows = soup.findAll('tr')
                for row in table_rows:
                    #For each row in the table rows, see if it is likely a row that contains
                    #the exhibit 21.1 (subsidiares) form. If it is, grab the URL and load the page
                    #
                    if re.search(EXHIBIT21_WORDS, row.text, re.IGNORECASE):
                        ex21_url = row.find('a').get('href')
                        try:
                            company.subsidiaries = self.get_exhibit21(BASE_URL + ex21_url)
                        except TypeError:
                            #Sometimes beautifulsoup trys to concatenate a str and None?
                            pass

                self.backend.add(company)


    def get_exhibit21(self, ex21_url):
        """
        Get the subsidiaries from the exhibit 21 filing and return them
        """
        subs = []
        contents = self.downloader.get_url(ex21_url)
        soup = BeautifulSoup(contents, convertEntities=BeautifulSoup.HTML_ENTITIES)

        
        #Assume that it's table based
        rows = soup.findAll('tr')
        for row in rows:
            tds = row.findChildren('td')
            subsidiary = self.get_subsidiary(tds)
            if subsidiary.name:
                subs.append(subsidiary)

        if len(subs) > 0:
            return subs


        #Otherwise this is not table based, assume the subs are in p
        #elements
        ps = soup.findAll('p')
        for p in ps:
            subsidiary = self.get_subsidiary(p.findAll())
            if subsidiary.name:
                subs.append(subsidiary)

        if len(subs) > 0:
            return subs
        

        #ps
        ps = soup.findAll('div')
        for p in ps:
            subsidiary = self.get_subsidiary(p.findAll())
            if subsidiary.name:
                subs.append(subsidiary)

        return subs




    #Takes a list of text and tries to get the subsidiary info out of it
    def get_subsidiary(self, lot):
        subsidiary = Company()
        lot = [snippet.text for snippet in lot]
        cmps = filter(lambda snippet : self.is_company(snippet), lot)
        for t in lot:
            s = self.get_state(t)
            if s:
                subsidiary.location = first_letter_caps(s)
        if not subsidiary.location:
            for t in lot:
                c = self.get_country(t)
                if c:
                    subsidiary.location = first_letter_caps(c)

        if len(cmps) > 0:
            subsidiary.name = clean_name(cmps[0])
        return subsidiary
        



    def clean(self, word):
        for j in JUNK:
            word = word.replace(j, "")
        return word

    def is_company(self, phrase):
        phrase = self.clean(phrase).lower()
        #TODO: think of a better wya to do this. Train it with a known data set and
        #create a more flexible approach as opposed to a bunch of regex hax, maybe?
        
        #If any of the "Company" key words appear near the end of the 
        #sentence, then this is probably a company. Not a very good approach. This is a
        #key method to this whole project, so it should be thought out btter
        regs = ['.*%s.{0,16}$'%c for c in CORPS]
        unregs = ['.*%s.{0,16}$'%c for c in EXCLUDE_CORPS]

        res = False
        for r in regs:
            if re.search(r, phrase):
                res = True
                break

        for r in unregs:
            if re.search(r, phrase):
                res = False
                break

        return res

    def get_state(self, word):
        word = self.clean(word)
        toks = word.lower().split()
        for t in toks:
            if t in STATES:
                return t
        return False

    def get_country(self, word):
        word = self.clean(word)
        toks = word.lower().split()
        for t in toks:
            if t in COUNTRIES:
                return t
        return False



    def company_found(self, text):
        return re.search(EXHIBIT21_WORDS, text, re.IGNORECASE) == None \
        and not re.search('SUBSIDIARIES', text) \
        and not re.search('&#160', text) \
        and len(text) > 3



    def extract_address(self, address_soup):
        els = address_soup.findAll()
        return (''.join([e.text + ", " for e in els])).strip(", ")


