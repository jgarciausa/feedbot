import unittest
from xml.etree import ElementTree

class BaseTest(unittest.TestCase):

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
        <status>
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
        </status>
        """.format(url1=self.url1, url2=self.url2, last_request_1=self.last_request_1,
                   last_request_2=self.last_request_2,
                   last_published_1=self.last_published_1, last_published_2=self.last_published_2))

