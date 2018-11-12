import unittest
from test import BaseTest
from feedbot.reader import FeedDataReader


class FeedDataReaderTest(BaseTest):

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
            self.assertFalse(feed.etag)

    def test_read_full(self):
        feed_config_reader = FeedDataReader(self.two_feed_full_tree)

        self.validate_feed_config_reader(feed_config_reader)

        self.assertEqual(feed_config_reader.feeds[0].last_request, self.last_request_1)
        self.assertEqual(feed_config_reader.feeds[0].last_published, self.last_published_1)
        self.assertEqual(feed_config_reader.feeds[0].etag, self.etag1)
        self.assertEqual(feed_config_reader.feeds[1].last_request, self.last_request_2)
        self.assertEqual(feed_config_reader.feeds[1].last_published, self.last_published_2)
        self.assertEqual(feed_config_reader.feeds[1].etag, self.etag2)


if __name__ == '__main__':
    unittest.main()
