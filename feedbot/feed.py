import feedparser
from feedparser import FeedParserDict
from dateutil import parser as dateparser
from datetime import datetime


class Feed:

    def __init__(self, url=None, last_request=None, etag=None, last_published=None):
        self.url = url
        self.last_request: datetime = last_request
        self.last_published: datetime = last_published
        self.etag: str = etag
        self.parsed_feed: FeedParserDict = None
        self._unpublished_items: list = []
        self._published_items: list = []

    def update_last_published(self):

        if not self._published_items:
            #  Do nothing.
            return

        for item in self._published_items:

            item_published: datetime = self._get_item_published(item)

            if not self.last_published or item_published > self.last_published:
                self.last_published = item_published

    @property
    def unpublished_items(self):

        if not self._unpublished_items:

            if not self.last_published:
                self._unpublished_items = self.parsed_feed['items']
            else:
                for item in self.parsed_feed['items']:

                    if self._get_item_published(item) > self.last_published:
                        self._unpublished_items.append(item)

        return self._unpublished_items

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

    def _get_item_published(self, item: FeedParserDict) -> datetime:
        return dateparser.parse(item['published'])

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

    @property
    def published_items(self):
        return self._published_items

    @published_items.setter
    def published_items(self, published_items):
        self._published_items = published_items

