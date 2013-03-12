from parser import Parser


class CorpCrawl(object):

	def __init__(self, backend, cache_path = ''):
		self.cache_path = cache_path
		self.backend = backend

	def crawl(self, years, quarters):
		parse = Parser(self.cache_path, self.backend)
		parse.parse(years, quarters)