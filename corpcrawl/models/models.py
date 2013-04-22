

class Company(object):

    name = None
    location = None
    business_address = None
    mailing_address = None
    exhibit21_url = None
    subsidiaries = []


    def __init__(self, *args, **kwargs):

        for k in kwargs.keys():
            setattr(self, k, kwargs[k])


    def __str__(self):
        return "Name: %s  mailing: %s \nsubs: %s" % \
        (self.name, self.mailing_address, '\n'.join([sub.name for sub in self.subsidiaries]))

