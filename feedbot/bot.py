import argparse
from xml.etree import ElementTree
from feedbot.reader import FeedDataReader

STATUS_XML_EMPTY = """<?xml version="1.0" ?>
<status>
    <feeds/>
</status>
"""


def main(config_tree, status_file, status_tree):
    config_data_reader = FeedDataReader(config_tree)
    status_data_reader = FeedDataReader(status_tree)

    for feed in config_data_reader.feeds:

        if feed.url in status_data_reader.indexed_feeds:
            feed.merge(status_data_reader.indexed_feeds.get(feed.url))

        feed.parse()

        for item in feed.unpublished_items:
            print("---------------------")
            print("Title: {title}".format(title=item['title']))
            print("Link: {link}".format(link=item['link']))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', "--config", help="location of config file")
    parser.add_argument('-s', "--status", help="location of status file")
    args = parser.parse_args()

    try:
        status_tree = ElementTree.parse(args.status)
    except FileNotFoundError:
        status_tree = ElementTree.fromstring(STATUS_XML_EMPTY)

    config_tree = ElementTree.parse(args.config)

    main(config_tree, args.status, status_tree)
