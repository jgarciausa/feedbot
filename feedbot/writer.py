from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from feedbot.feed import Feed
from xml.dom import minidom


class FeedDataWriter:

    def __init__(self, feeds):
        self.feeds: list = feeds
        self._status: Element = self._generate_status()
        self._pretty_xml = self._get_pretty_xml()

    @property
    def status(self) -> Element:
        return self._status

    @property
    def pretty_xml(self) -> str:
        return self._pretty_xml

    def _get_pretty_xml(self):
        rough_string = ElementTree.tostring(self.status, 'utf-8')
        parsed = minidom.parseString(rough_string)
        pretty = parsed.toprettyxml(indent="    ")
        return pretty

    def _generate_status(self) -> Element:

        #  Create top-level element.
        status: Element = Element('status')
        feeds_element: Element = SubElement(status, 'feeds')

        #  If we have no feeds, ...
        if not self.feeds:
            #  return an empty ElementTree.
            return status

        for feed in self.feeds:

            feed_element: Element = self._generate_feed_element(feed)

            if feed_element:
                feeds_element.append(feed_element)

        #  Start with an empty ElementTree.
        return status

    def _generate_feed_element(self, feed: Feed) -> Element:

        if not feed.url:
            return None

        feed_element: Element = Element('feed')

        self._set_element_text(SubElement(feed_element, 'url'), feed.url)

        if feed.last_request:
            self._set_element_text(SubElement(feed_element, 'last_request'), feed.last_request)
        if feed.etag:
            self._set_element_text(SubElement(feed_element, 'etag'), feed.etag)
        if feed.last_published:
            self._set_element_text(SubElement(feed_element, 'last_published'), feed.last_published.isoformat())

        return feed_element

    def _set_element_text(self, element: Element, text: str):
        element.text = text