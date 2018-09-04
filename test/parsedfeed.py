from feedparser import FeedParserDict

PARSED_FEED_304: FeedParserDict = FeedParserDict()
PARSED_FEED_304['status'] = 304
PARSED_FEED_304['feed'] = {}
PARSED_FEED_304['entries'] = []
PARSED_FEED_304['debug_message'] = ('The feed has not changed since you last checked, so the server sent no '
                                    'data.  This is a feature, not a bug!')
