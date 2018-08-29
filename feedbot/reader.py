from feedbot.feed import Feed

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
            last_published = self._get_child_node_text(feed, "./last_published")

            self.feeds.append(Feed(url, last_request, last_published))