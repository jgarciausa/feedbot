import unittest
from feedbot.config import FeedConfigReader
from xml.etree import ElementTree


class FeedConfigReaderTest(unittest.TestCase):

    def setUp(self):
        self.url1 = 'http://rss.nytimes.com/services/xml/rss/nyt/NYRegion.xml'
        self.url2 = 'http://www.nydailynews.com/cmlink/NYDN.Local.rss'
        self.two_feed_tree = ElementTree.fromstring("""<?xml version="1.0"?>
<config>
    <feeds>
        <feed>
            <url>{url1}</url>
        </feed>
        <feed>
            <url>{url2}</url>
        </feed>
    </feeds>
</config>
""".format(url1=self.url1, url2=self.url2))
        self.feedConfigReader = FeedConfigReader(self.two_feed_tree)

    def test_read_correct_number_of_feeds(self):
        self.assertEqual(len(self.feedConfigReader.feeds), 2)
        self.assertTrue(self.feedConfigReader.feeds[0])
        self.assertEqual(self.feedConfigReader.feeds[0].url, self.url1)
        self.assertEqual(self.feedConfigReader.feeds[1].url, self.url2)

        for feed in self.feedConfigReader.feeds:
            self.assertFalse(feed.last_request)
            self.assertFalse(feed.last_published)


if __name__ == '__main__':
    unittest.main()
