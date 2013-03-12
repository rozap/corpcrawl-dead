

class Company(object):

    name = None
    location = None
    business_address = None
    mailing_address = None
    subsidiaries = []


    def __init__(self, *args, **kwargs):
        for k in kwargs.keys():
            self.setattr(k, kwargs[k])


    def __str__(self):
        return "Name: %s  mailing: %s \nsubs: %s" % \
        (self.name.encode('utf-8'), self.mailing_address.encode('utf-8'), '\n'.join([sub.name.encode('utf-8') for sub in self.subsidiaries]))

