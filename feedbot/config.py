from feedbot.feed import Feed

class FeedConfigReader:

    def __init__(self, tree):
        self.feeds = []
        self._get_feed_data(tree)

    def _get_feed_data(self, tree):
        feeds = tree.findall("./feeds/feed")
        for feed in feeds:
            url = feed.find("./url").text
            self.feeds.append(Feed(url))