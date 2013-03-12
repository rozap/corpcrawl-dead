import urllib2
import re
import hashlib
from zipfile import ZipFile
from StringIO import StringIO
import os

class Downloader(object):

    def __init__(self, cache_path):
        self.cache_path = cache_path


    def get_idx(self, year, quarter):
        url = "ftp://ftp.sec.gov/edgar/full-index/%s/QTR%d/form.zip" % (year, quarter)


        dir_name = '%sdata/%d/' % (self.cache_path, year)
        file_name = 'form_qtr%d.idx'% quarter

        try:
            pass
        except IOError as e:
            z_file = urllib2.urlopen(url % (year, quarter)).read()
            zip_file = ZipFile(StringIO(z_file))
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            with open(dir_name + file_name, 'w+') as output:
                output.write(zip_file.read('form.idx'))

        with open(dir_name + file_name) as cached:
                return cached.readlines()


    def get_url(self, url):
        file_name = hashlib.md5(url).hexdigest()
        dir_name = '%spages/cache/' % self.cache_path
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        try:
            with open(dir_name + file_name, 'r') as f:
                return f.read()
        except IOError as e:
            return self.__download(dir_name + file_name, url)

    def purge(self, url):
        file_name = hashlib.md5(url).hexdigest()
        dir_name = '%spages/cache/' % self.cache_path
        os.remove(dir_name + file_name)

    def __download(self, file_name, url):
        with open(file_name, 'w+') as f:
            contents = urllib2.urlopen(url).read()
            f.write(contents)
            return contents