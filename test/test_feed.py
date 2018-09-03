import unittest

from test import BaseTest
from test import PARSED_FEED_304
from feedbot.feed import Feed
from unittest.mock import patch


class FeedTest(BaseTest):

    feed: Feed

    def setUp(self):
        super().setUp()
        self.feed = Feed()

    @patch('feedparser.parse', return_value=PARSED_FEED_304)
    def test_parse_feed_has_etag_and_modified_expect_304(self, parse):
        feed: Feed = Feed(self.url1, self.last_request_1, self.last_published_1, self.etag1)
        feed.parse()

        self.assertIsNotNone(feed.parsed_feed)
        self.assertEqual(feed.last_request, self.last_request_1)

    def test_merge_parameter_is_None(self):
        self.assertRaises(RuntimeError, self.feed.merge, None)

    def test_merge_from_object_is_full(self):

        from_feed: Feed = Feed(self.url1, self.last_request_1, self.last_published_1, self.etag1)
        to_feed: Feed = Feed(self.url2, self.last_request_2, self.last_published_2, self.etag2)

        from_feed.merge(to_feed)

        self.validate_feed_expect_values1(from_feed)

    def test_merge_from_object_is_empty(self):

        to_feed: Feed = Feed(self.url1, self.last_request_1, self.last_published_1, self.etag1)

        self.feed.merge(to_feed)

        self.validate_feed_expect_values1(self.feed)

    def test_merge_from_object_some_None_some_not_None(self):
        from_feed: Feed = Feed(None, self.last_request_1, None, self.etag1)
        to_feed: Feed = Feed(self.url2, self.last_request_2, self.last_published_2, self.etag2)

        from_feed.merge(to_feed)

        self.assertEqual(from_feed.url, self.url2)
        self.assertEqual(from_feed.last_request, self.last_request_1)
        self.assertEqual(from_feed.last_published, self.last_published_2)
        self.assertEqual(from_feed.etag, self.etag1)

    def validate_feed_expect_values1(self, from_feed):
        self.assertEqual(from_feed.url, self.url1)
        self.assertEqual(from_feed.last_request, self.last_request_1)
        self.assertEqual(from_feed.last_published, self.last_published_1)
        self.assertEqual(from_feed.etag, self.etag1)


if __name__ == '__main__':
    unittest.main()
