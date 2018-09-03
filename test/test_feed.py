import unittest
from test import BaseTest
from feedbot.feed import Feed


class FeedTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.feed = Feed()

    def test_merge_parameter_is_None(self):
        self.assertRaises(RuntimeError, self.feed.merge, None)

    def test_merge_from_object_is_full(self):

        from_feed: Feed = Feed(self.url1, self.last_request_1, self.last_published_1)
        to_feed: Feed = Feed(self.url2, self.last_request_2, self.last_published_2)

        from_feed.merge(to_feed)

        self.assertEquals(from_feed.url, self.url1)
        self.assertEqual(from_feed.last_request, self.last_request_1)
        self.assertEqual(from_feed.last_published, self.last_published_1)

    def test_merge_from_object_is_empty(self):

        from_feed: Feed = Feed()
        to_feed: Feed = Feed(self.url1, self.last_request_1, self.last_published_1)

        from_feed.merge(to_feed)

        self.assertEquals(from_feed.url, self.url1)
        self.assertEqual(from_feed.last_request, self.last_request_1)
        self.assertEqual(from_feed.last_published, self.last_published_1)

    def test_merge_from_object_some_None_some_not_None(self):
        from_feed: Feed = Feed(None, self.last_request_1, None)
        to_feed: Feed = Feed(self.url2, self.last_request_2, self.last_published_2)

        from_feed.merge(to_feed)

        self.assertEquals(from_feed.url, self.url2)
        self.assertEqual(from_feed.last_request, self.last_request_1)
        self.assertEqual(from_feed.last_published, self.last_published_2)


if __name__ == '__main__':
    unittest.main()
