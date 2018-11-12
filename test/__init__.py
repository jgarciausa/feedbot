import unittest
from xml.etree import ElementTree
from xml.sax.saxutils import escape
from feedbot.bot import STATUS_XML_EMPTY


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.url1 = 'http://rss.nytimes.com/services/xml/rss/nyt/NYRegion.xml'
        self.url2 = 'http://www.nydailynews.com/cmlink/NYDN.Local.rss'
        self.config_tree: ElementTree = ElementTree.fromstring("""<?xml version="1.0"?>
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

        self.last_request_1 = 'Mon, 03 Sep 2018 21:51:12 GMT'
        self.last_published_1 = '2018-09-03T21:46:12+00:00'
        self.etag1 = '"d72ddde07efac3b2fc37ff5f42751fc66"'
        self.last_request_2 = 'Mon, 03 Sep 2018 19:51:12 GMT'
        self.last_published_2 = '2018-09-03T19:46:12+00:00'
        self.etag2 = '"66cf15724f5ff73cf2b3cafe70edd27d"'

        self.escape_dict = {'"': '&quot;'}

        self.status_tree_string = """<?xml version="1.0" ?>
<status>
    <feeds>
        <feed>
            <url>{url1}</url>
            <last_request>{last_request_1}</last_request>
            <etag>{etag1}</etag>
            <last_published>{last_published_1}</last_published>
        </feed>
        <feed>
            <url>{url2}</url>
            <last_request>{last_request_2}</last_request>
            <etag>{etag2}</etag>
            <last_published>{last_published_2}</last_published>
        </feed>
    </feeds>
</status>
""".format(url1=self.url1, last_request_1=self.last_request_1, etag1=escape(self.etag1, self.escape_dict),
                   last_published_1=self.last_published_1, url2=self.url2, last_request_2=self.last_request_2,
                   etag2=escape(self.etag2, self.escape_dict), last_published_2=self.last_published_2)

        self.status_tree_full = ElementTree.fromstring(self.status_tree_string)

        self.status_tree_empty = ElementTree.fromstring(STATUS_XML_EMPTY)

        self.status_xml_no_feeds = """<?xml version="1.0" ?>
<status>
    <feeds/>
</status>
"""
