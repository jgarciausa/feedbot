import unittest
from test import BaseTest
from feedbot.writer import FeedDataWriter

class FeedDataReaderTest(BaseTest):

    def test_write_feed_list_is_none(self):

        feed_data_writer = FeedDataWriter(None)

        self.assertEqual(self.status_xml_no_feeds, feed_data_writer.pretty_xml)

    def test_write_feed_list_is_empty_list(self):

        feed_data_writer = FeedDataWriter([])

        self.assertEqual(self.status_xml_no_feeds, feed_data_writer.pretty_xml)


if __name__ == '__main__':
    unittest.main()
