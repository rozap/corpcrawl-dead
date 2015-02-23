

this is dead, see rozap/corpcrawl

corpcrawl
=============

About
-----
This is a python scraper for the Securities and Exchange Commission EDGAR database. It looks at the Form 10k
filings that publicly held corporations are required to file with the SEC. It then attempts to extract the 
subsidiary relationships from the 10k exhibit 21.1. 

Corpcrawl is a storage agnostic scraper, so you'll need to implement your own storage scheme. 


Installation
------------
You can get the package from PyPi through Pip. 
    
    pip install corpcrawl
    
From a python console you can try

    import corpcrawl
    
If it works, then you can get started


Running it
----------
First import the required pieces

    
    from corpcrawl.crawler import CorpCrawl

    from corpcrawl.backend import Backend
    
    def main()
        my_backend = MyBackend()
        crawler = CorpCrawl(cache_path = '/an/absolute/path/to/some/dir', backend = my_backend)
        c.crawl(years = [2011, 2012], quarters = [1, 2, 3, 4])
    
    
    class MyBackend(Backend):

        def get_company(self, name):
            pass

        def add_company(self, comp):
            print "Adding %s" % str(comp)
            
            
            
            
            
            
This is about as simple of a backend as can be. This code will crawl the filings and print out the name of each
company and subsidiary that it finds for all quarters of years 2011 and 2012.
Obviously you will want to hook it up to a database or something.

Notes
-----
The SEC data is very unstructured. As such, there are a lot of errors. This is version 0.0.1, so instead of
implementing your own methods to massage the data that it returns, it would be better if you could contribute
so make the core parser better. 
