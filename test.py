
from corpcrawl.crawler import CorpCrawl
from corpcrawl.backend import Backend

def main():
    backend = MyBackend()
    c = CorpCrawl(cache_path = '/home/chris/corpcrawl', backend = backend)
    c.crawl()




class MyBackend(Backend):

    def get_company(self, name):
        pass

    def add_company(self, comp):
        print "Adding %s" % str(comp)


if __name__ == '__main__':
    main()