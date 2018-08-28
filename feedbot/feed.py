class Feed:

    def __init__(self, url, last_request=None, last_published=None):
        self.url = url
        self.last_request = last_request
        self.last_published = last_published

