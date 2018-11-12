from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from feedbot.feed import Feed


class FeedDataWritter:

    def __init__(self, feeds):
        self.feeds: list = feeds
        self.tree: ElementTree = self._generate_tree()

    def _generate_tree(self) -> ElementTree:

        #  Start with an empty ElementTree.
        element_tree: ElementTree = ElementTree()

        #  Add elements.
        status: Element = element_tree.Element('status')
        feeds_element: Element = element_tree.SubElement(status, 'feeds')

        #  If we have no feeds, ...
        if not self.feeds:
            #  return an empty ElementTree.
            return element_tree

        for feed in self.feeds:

            if not feed.url:
                continue

            feeds_element.append(self._generate_feed_element(feed))

    def _generate_feed_element(self, feed: Feed) -> Element:
        feed_element: Element = Element('feed')
        self._set_element_text(SubElement(feed_element, 'url'), feed.url)
        self._set_element_text(SubElement(feed_element, 'last_request'), feed.last_request)
        self._set_element_text(SubElement(feed_element, 'etag'), feed.etag)
        self._set_element_text(SubElement(feed_element, 'last_published'), feed.last_published.isoformat())

        return feed_element

    def _set_element_text(self, element: Element, text: str):
        element.text = text