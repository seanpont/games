__author__ = 'tron'

from HTMLParser import HTMLParser
from urllib2 import urlopen
from collections import namedtuple
import functional as f


attrs = [('href', '/wiki/Affenpinscher'), ('title', 'Affenpinscher')]

def map_attrs(attrs):
    """
    :param attrs: tag attrs as list of key/value pairs
    :return: a map of key: value
    """
    return reduce(lambda m, kv: f.set_on(m, kv[0], kv[1]), attrs, {})

print map_attrs(attrs)


DogBreed = namedtuple('DogBreed', 'name url origin group image_url')


class DogBreedDownloader(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.breeds = []
        self.name = ''
        self.url = ''
        self.origin = ''
        self.group = ''
        self.image_url = ''
        self.td_count = -1
        self.in_name_url = False
        self.in_origin_url = False
        self.in_group_tag = False
        self.in_first_table = True

    def handle_starttag(self, tag, attrs):
        if not self.in_first_table:
            return

        if tag == 'td':
            self.td_count += 1

        if self.td_count == 0 and tag == 'a':
            self.in_name_url = True
            attr_map = map_attrs(attrs)
            if 'href' in attr_map:
                self.url = "https://en.wikipedia.org" + attr_map['href']
        elif self.td_count == 1 and tag == 'a':
            self.in_origin_url = True
        elif self.td_count == 8:
            self.in_group_tag = True
        elif self.td_count == 9 and tag == 'img':
            self.image_url = 'https:' + filter(lambda attr: attr[0] == 'src', attrs)[0][1]

    def handle_data(self, data):
        if not self.in_first_table:
            return
        if self.in_name_url:
            self.name += data
            self.in_name_url = False
        elif self.in_origin_url:
            self.origin += ' ' + data
            self.in_origin_url = False
        elif self.in_group_tag:
            self.group += data
            self.in_group_tag = False

    def handle_endtag(self, tag):
        if not self.in_first_table:
            return

        if tag == 'table':
            self.in_first_table = False
        elif tag == 'tr':
            self.breeds.append(
                DogBreed(self.name.strip(),
                         self.url.strip(),
                         self.origin.strip(),
                         self.group.strip(),
                         self.image_url.strip()))
            self.td_count = -1
            self.name = ''
            self.url = ''
            self.origin = ''
            self.group = ''
            self.image_url = ''

    def download_breeds(self):
        """
        :return: list of DogBreeds from wikipedia
        """
        dog_breeds_url = "https://en.wikipedia.org/wiki/List_of_dog_breeds"
        print 'Downloading breeds from %s' % dog_breeds_url
        dog_breeds_html = urlopen(dog_breeds_url).read()
        print 'Parsing html...'
        self.feed(dog_breeds_html)
        return self.breeds[1:]
