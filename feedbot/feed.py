import feedparser
from feedparser import FeedParserDict

class Feed:

    def __init__(self, url=None, last_request=None, last_published=None, etag=None):
        self.url = url
        self.last_request = last_request
        self.last_published = last_published
        self.etag = etag
        self.parsed_feed: FeedParserDict = None

    def parse(self):

        self.parsed_feed = self._get_parsed_feed()

        if self.parsed_feed.has_key('modified'):
            self.last_request = self.parsed_feed.modified
        if self.parsed_feed.has_key('etag'):
            self.etag = self.parsed_feed.etag

    def merge(self, feed):
        if not feed:
            raise RuntimeError("Invalid parameter!")
        #  Loop through all the object's attributes.
        for attr, value in self.__dict__.items():
            #  If the object doesn't have a value for this attribute AND the object passed in DOES have a value, ...
            if not self.__dict__[attr] and feed.__dict__[attr]:
                #  Set it for this object.
                self.__dict__[attr] = feed.__dict__[attr]

    def _get_parsed_feed(self):
        if not self.etag and not self.last_request:
            return feedparser.parse(self.url)
        #  Always use etag if available.
        if self.etag:
            return feedparser.parse(self.url, etag=self.etag)
        #  If there's no etag but we do have a last_request
        if not self.etag and self.last_request:
            #  ... pass in the last_request as the modified
            return feedparser.parse(self.url, modified=self.last_request)

