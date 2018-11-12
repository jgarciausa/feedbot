import unittest

from test import BaseTest
from test.parsedfeed import PARSED_FEED_304
from test.parsedfeed import NYT_PARSED_FEED_200
from test.parsedfeed import NYT_VALID_RESPONSE_LAST_MODIFIED
from test.parsedfeed import NYT_VALID_RESPONSE_ETAG
from test.parsedfeed import NYT_EXPECTED_VALUES
from test.parsedfeed import ITEM_TEST_KEYS
from test.parsedfeed import NYT_LAST_PUBLISHED_BEFORE_ALL_ITEMS
from test.parsedfeed import NYT_LAST_PUBLISHED_MIDPOINT_OF_ITEMS
from test.parsedfeed import NYT_LAST_PUBLISHED_ONLY_ONE_ITEM_AFTER
from test.parsedfeed import NYT_LAST_PUBLISHED_AFTER_ALL_ITEMS
from test.parsedfeed import NYT_LATEST_PUB_DATE_DATETIME

from feedbot.feed import Feed
from unittest.mock import patch
from xml.sax.saxutils import unescape
from dateutil import parser as dateparser
import datetime


class FeedTest(BaseTest):

    feed: Feed

    def setUp(self):
        super().setUp()
        self.feed = Feed()

    @patch('feedparser.parse', return_value=NYT_PARSED_FEED_200)
    def test_parse_feed_no_etag_no_modified_expect_200(self, parse):
        feed: Feed = Feed(self.url1, None, None, self.last_published_1)
        feed.parse()

        self.assertIsNotNone(feed.parsed_feed)
        self.assertEqual(feed.last_request, NYT_VALID_RESPONSE_LAST_MODIFIED)
        self.assertEqual(feed.etag, NYT_VALID_RESPONSE_ETAG)

    @patch('feedparser.parse', return_value=NYT_PARSED_FEED_200)
    def test_parse_nyt_valid_feed_items(self, parse):
        feed: Feed = Feed(self.url1, None, None, None)
        feed.parse()

        self.assertIsNotNone(feed.parsed_feed)
        self.assertTrue(feed.parsed_feed.has_key('items'))

        expected_items_size = len(NYT_EXPECTED_VALUES)

        self.assertEqual(expected_items_size, len(feed.parsed_feed['items']))

        for a in range(expected_items_size):
            self.assertIsNotNone(feed.parsed_feed['items'][a])
            item_dict = feed.parsed_feed['items'][a]
            self.assertIsNotNone(NYT_EXPECTED_VALUES[a])
            expected_values = NYT_EXPECTED_VALUES[a]

            for key in ITEM_TEST_KEYS:
                self.assertEqual(unescape(expected_values[key]), item_dict[key])

    @patch('feedparser.parse', return_value=NYT_PARSED_FEED_200)
    def test_update_last_published_nyt_valid_feed_last_published_is_none(self, parse):

        #  Start with the last_published set to None.
        feed: Feed = Feed(self.url1, None, None, None)
        feed.parse()

        self.assertIsNotNone(feed.parsed_feed)
        self.assertTrue(feed.parsed_feed.has_key('items'))

        feed.published_items = feed.unpublished_items

        feed.update_last_published()

        self.assertEqual(NYT_LATEST_PUB_DATE_DATETIME, feed.last_published)

    @patch('feedparser.parse', return_value=NYT_PARSED_FEED_200)
    def test_update_last_published_nyt_valid_feed_last_published_is_before_all_items(self, parse):

        last_published: datetime.datetime = dateparser.parse(NYT_LAST_PUBLISHED_BEFORE_ALL_ITEMS)

        #  Start with the last_published set to None.
        feed: Feed = Feed(self.url1, None, None, last_published)
        feed.parse()

        self.assertIsNotNone(feed.parsed_feed)
        self.assertTrue(feed.parsed_feed.has_key('items'))

        feed.published_items = feed.unpublished_items

        feed.update_last_published()

        self.assertEqual(NYT_LATEST_PUB_DATE_DATETIME, feed.last_published)

    @patch('feedparser.parse', return_value=NYT_PARSED_FEED_200)
    def test_update_last_published_nyt_valid_feed_last_published_is_midpoint_of_items(self, parse):

        last_published: datetime.datetime = dateparser.parse(NYT_LAST_PUBLISHED_MIDPOINT_OF_ITEMS)

        #  Start with the last_published set to None.
        feed: Feed = Feed(self.url1, None, None, last_published)
        feed.parse()

        self.assertIsNotNone(feed.parsed_feed)
        self.assertTrue(feed.parsed_feed.has_key('items'))

        feed.published_items = feed.unpublished_items

        feed.update_last_published()

        self.assertEqual(NYT_LATEST_PUB_DATE_DATETIME, feed.last_published)

    @patch('feedparser.parse', return_value=NYT_PARSED_FEED_200)
    def test_update_last_published_nyt_valid_feed_last_published_is_only_one_item_after(self, parse):

        last_published: datetime.datetime = dateparser.parse(NYT_LAST_PUBLISHED_ONLY_ONE_ITEM_AFTER)

        #  Start with the last_published set to None.
        feed: Feed = Feed(self.url1, None, None, last_published)
        feed.parse()

        self.assertIsNotNone(feed.parsed_feed)
        self.assertTrue(feed.parsed_feed.has_key('items'))

        feed.published_items = feed.unpublished_items

        feed.update_last_published()

        self.assertEqual(NYT_LATEST_PUB_DATE_DATETIME, feed.last_published)

    @patch('feedparser.parse', return_value=NYT_PARSED_FEED_200)
    def test_update_last_published_nyt_valid_feed_last_published_is_after_all_items(self, parse):

        last_published: datetime.datetime = dateparser.parse(NYT_LAST_PUBLISHED_AFTER_ALL_ITEMS)

        #  Start with the last_published set to None.
        feed: Feed = Feed(self.url1, None, None, last_published)
        feed.parse()

        self.assertIsNotNone(feed.parsed_feed)
        self.assertTrue(feed.parsed_feed.has_key('items'))

        feed.published_items = feed.unpublished_items

        feed.update_last_published()

        self.assertEqual(last_published, feed.last_published)

    @patch('feedparser.parse', return_value=NYT_PARSED_FEED_200)
    def test_unpublished_items_nyt_valid_feed_last_published_is_none(self, parse):
        feed: Feed = Feed(self.url1, None, None, None)
        feed.parse()

        self.assertIsNotNone(feed.parsed_feed)
        self.assertTrue(feed.parsed_feed.has_key('items'))

        all_items = feed.parsed_feed['items']

        self.assertEqual(all_items, feed.unpublished_items)

    @patch('feedparser.parse', return_value=NYT_PARSED_FEED_200)
    def test_unpublished_items_nyt_valid_feed_last_published_is_before_all_items(self, parse):

        last_published: datetime.datetime = dateparser.parse(NYT_LAST_PUBLISHED_BEFORE_ALL_ITEMS)

        feed: Feed = Feed(self.url1, None, None, last_published)
        feed.parse()

        self.assertIsNotNone(feed.parsed_feed)
        self.assertTrue(feed.parsed_feed.has_key('items'))

        all_items = feed.parsed_feed['items']

        self.assertEqual(all_items, feed.unpublished_items)

    @patch('feedparser.parse', return_value=NYT_PARSED_FEED_200)
    def test_unpublished_items_nyt_valid_feed_last_published_is_midpoint_of_items(self, parse):

        last_published: datetime.datetime = dateparser.parse(NYT_LAST_PUBLISHED_MIDPOINT_OF_ITEMS)

        feed: Feed = Feed(self.url1, None, None, last_published)
        feed.parse()

        self.assertIsNotNone(feed.parsed_feed)
        self.assertTrue(feed.parsed_feed.has_key('items'))

        self.assertEqual(2, len(feed.unpublished_items))

    @patch('feedparser.parse', return_value=NYT_PARSED_FEED_200)
    def test_unpublished_items_nyt_valid_feed_last_published_is_only_one_item_after(self, parse):

        last_published: datetime.datetime = dateparser.parse(NYT_LAST_PUBLISHED_ONLY_ONE_ITEM_AFTER)

        feed: Feed = Feed(self.url1, None, None, last_published)
        feed.parse()

        self.assertIsNotNone(feed.parsed_feed)
        self.assertTrue(feed.parsed_feed.has_key('items'))

        self.assertEqual(1, len(feed.unpublished_items))

    @patch('feedparser.parse', return_value=NYT_PARSED_FEED_200)
    def test_unpublished_items_nyt_valid_feed_last_published_is_after_all_items(self, parse):

        last_published: datetime.datetime = dateparser.parse(NYT_LAST_PUBLISHED_AFTER_ALL_ITEMS)

        feed: Feed = Feed(self.url1, None, None, last_published)
        feed.parse()

        self.assertIsNotNone(feed.parsed_feed)
        self.assertTrue(feed.parsed_feed.has_key('items'))

        self.assertFalse(feed.unpublished_items)

    @patch('feedparser.parse', return_value=PARSED_FEED_304)
    def test_parse_feed_has_etag_and_modified_expect_304(self, parse):
        feed: Feed = Feed(self.url1, self.last_request_1, self.etag1, self.last_published_1)
        feed.parse()

        self.assertIsNotNone(feed.parsed_feed)
        self.assertEqual(feed.last_request, self.last_request_1)
        self.assertEqual(feed.etag, self.etag1)

    def test_merge_parameter_is_None(self):
        self.assertRaises(RuntimeError, self.feed.merge, None)

    def test_merge_from_object_is_full(self):

        from_feed: Feed = Feed(self.url1, self.last_request_1, self.etag1, self.last_published_1)
        to_feed: Feed = Feed(self.url2, self.last_request_2, self.etag2, self.last_published_2)

        from_feed.merge(to_feed)

        self.validate_feed_expect_values1(from_feed)

    def test_merge_from_object_is_empty(self):

        to_feed: Feed = Feed(self.url1, self.last_request_1, self.etag1, self.last_published_1)

        self.feed.merge(to_feed)

        self.validate_feed_expect_values1(self.feed)

    def test_merge_from_object_some_None_some_not_None(self):
        from_feed: Feed = Feed(None, self.last_request_1, self.etag1, None)
        to_feed: Feed = Feed(self.url2, self.last_request_2, self.etag2, self.last_published_2)

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
