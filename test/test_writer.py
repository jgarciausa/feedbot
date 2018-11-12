import unittest
from test import BaseTest
from feedbot.writer import FeedDataWriter
from feedbot.feed import Feed
from dateutil import parser as dateparser


class FeedDataReaderTest(BaseTest):

    def test_write_feed_list_is_none(self):

        feed_data_writer = FeedDataWriter(None)

        self.assertEqual(self.status_xml_no_feeds, feed_data_writer.pretty_xml)

    def test_write_feed_list_is_empty_list(self):

        feed_data_writer = FeedDataWriter([])

        self.assertEqual(self.status_xml_no_feeds, feed_data_writer.pretty_xml)

    def test_write_feed_list_has_two_feeds(self):

        feeds = [Feed(self.url1, self.last_request_1, self.etag1, dateparser.parse(self.last_published_1)),
                 Feed(self.url2, self.last_request_2, self.etag2, dateparser.parse(self.last_published_2))]

        feed_data_writer = FeedDataWriter(feeds)

        self.assertEqual(self.status_tree_string, feed_data_writer.pretty_xml)


if __name__ == '__main__':
    unittest.main()
