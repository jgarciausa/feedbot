import unittest
from feedbot.reader import FeedDataReader
from xml.etree import ElementTree


class FeedDataReaderTest(unittest.TestCase):

    def setUp(self):
        self.url1 = 'http://rss.nytimes.com/services/xml/rss/nyt/NYRegion.xml'
        self.url2 = 'http://www.nydailynews.com/cmlink/NYDN.Local.rss'
        self.two_feed_url_only_tree = ElementTree.fromstring("""<?xml version="1.0"?>
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

        self.last_request_1 = '2018-08-29T02:43:36.247607+00:00'
        self.last_published_1 = '2018-08-29T02:40:36.247607+00:00'
        self.last_request_2 = '2018-08-29T02:43:38.247607+00:00'
        self.last_published_2 = '2018-08-29T02:38:36.247607+00:00'

        self.two_feed_full_tree = ElementTree.fromstring("""<?xml version="1.0"?>
    <config>
        <feeds>
            <feed>
                <url>{url1}</url>
                <last_request>{last_request_1}</last_request>
                <last_published>{last_published_1}</last_published>
            </feed>
            <feed>
                <url>{url2}</url>
                <last_request>{last_request_2}</last_request>
                <last_published>{last_published_2}</last_published>
            </feed>
        </feeds>
    </config>
    """.format(url1=self.url1, url2=self.url2, last_request_1=self.last_request_1, last_request_2=self.last_request_2, last_published_1=self.last_published_1, last_published_2=self.last_published_2))

    def validate_feed_config_reader(self, feed_config_reader):
        self.assertEqual(len(feed_config_reader.feeds), 2)
        self.assertTrue(feed_config_reader.feeds[0])
        self.assertEqual(feed_config_reader.feeds[0].url, self.url1)
        self.assertEqual(feed_config_reader.feeds[1].url, self.url2)

    def test_read_url_only(self):
        feed_config_reader = FeedDataReader(self.two_feed_url_only_tree)

        self.validate_feed_config_reader(feed_config_reader)

        for feed in feed_config_reader.feeds:
            self.assertFalse(feed.last_request)
            self.assertFalse(feed.last_published)

    def test_read_full(self):
        feed_config_reader = FeedDataReader(self.two_feed_full_tree)

        self.validate_feed_config_reader(feed_config_reader)

        self.assertEqual(feed_config_reader.feeds[0].last_request, self.last_request_1)
        self.assertEqual(feed_config_reader.feeds[0].last_published, self.last_published_1)
        self.assertEqual(feed_config_reader.feeds[1].last_request, self.last_request_2)
        self.assertEqual(feed_config_reader.feeds[1].last_published, self.last_published_2)


if __name__ == '__main__':
    unittest.main()
