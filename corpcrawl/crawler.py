from parser import Parser


class CorpCrawl(object):

	def __init__(self, backend, cache_path = ''):
		print "Created Crawler"
		self.cache_path = cache_path
		self.backend = backend

	def crawl(self):
		print "Beginning Crawl"
		parse = Parser(self.cache_path, self.backend)
		parse.parse()