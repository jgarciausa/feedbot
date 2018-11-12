import unittest
from test import BaseTest
from feedbot.reader import FeedDataReader


class FeedDataReaderTest(BaseTest):

    def test_read_config(self):
        feed_config_reader = FeedDataReader(self.config_tree)

        self.validate_feed_config_reader(feed_config_reader)

        for feed in feed_config_reader.feeds:
            self.assertFalse(feed.last_request)
            self.assertFalse(feed.last_published)
            self.assertFalse(feed.etag)

    def test_read_status_full(self):
        feed_config_reader = FeedDataReader(self.status_tree_full)

        self.validate_feed_config_reader(feed_config_reader)

        self.assertEqual(feed_config_reader.feeds[0].last_request, self.last_request_1)
        self.assertEqual(feed_config_reader.feeds[0].last_published.isoformat(), self.last_published_1)
        self.assertEqual(feed_config_reader.feeds[0].etag, self.etag1)
        self.assertEqual(feed_config_reader.feeds[1].last_request, self.last_request_2)
        self.assertEqual(feed_config_reader.feeds[1].last_published.isoformat(), self.last_published_2)
        self.assertEqual(feed_config_reader.feeds[1].etag, self.etag2)

    def test_read_status_empty(self):
        feed_config_reader = FeedDataReader(self.status_tree_empty)

        self.assertFalse(feed_config_reader.feeds)

    def validate_feed_config_reader(self, feed_config_reader):
        self.assertEqual(len(feed_config_reader.feeds), 2)
        self.assertTrue(feed_config_reader.feeds[0])
        self.assertEqual(feed_config_reader.feeds[0].url, self.url1)
        self.assertEqual(feed_config_reader.feeds[1].url, self.url2)


if __name__ == '__main__':
    unittest.main()
