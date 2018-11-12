from feedbot.feed import Feed
from dateutil import parser as dateparser


class FeedDataReader:

    def __init__(self, tree):
        self.feeds = []
        self._get_feed_data(tree)

    def _get_child_node_text(self, node, xpath):
        child_node = node.find(xpath)
        if child_node is not None:
            return child_node.text

    def _get_feed_data(self, tree):
        feeds = tree.findall("./feeds/feed")
        for feed in feeds:

            url = self._get_child_node_text(feed, "./url")
            last_request = self._get_child_node_text(feed, "./last_request")
            last_published_string = self._get_child_node_text(feed, "./last_published")
            if last_published_string:
                last_published = dateparser.parse(last_published_string)
            else:
                last_published = None
            etag = self._get_child_node_text(feed, "./etag")

            self.feeds.append(Feed(url, last_request=last_request, etag=etag, last_published=last_published))