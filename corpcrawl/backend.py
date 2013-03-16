


class Backend(object):

	def __init__(self):
		pass

	def clean(self, company):
		
		def clean_atts(c):
			c.name = c.name.encode('utf-8') if c.name else None
			c.location = c.location.encode('utf-8') if c.location else None
			c.mailing_address = c.mailing_address.encode('utf-8') if c.mailing_address else None
			c.business_address = c.business_address.encode('utf-8') if c.business_address else None
			return c

		company = clean_atts(company)
		company.subsidiaries = [clean_atts(sub) for sub in company.subsidiaries]

		return company

	def get_company(self, name):
		raise NotImplementedError('You need to subclass this')

	def add(self, company):
		self.add_company(self.clean(company))

	def add_company(self, company):
		raise NotImplementedError('You need to subclass this')