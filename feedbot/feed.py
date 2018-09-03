class Feed:

    def __init__(self, url=None, last_request=None, last_published=None):
        self.url = url
        self.last_request = last_request
        self.last_published = last_published

    def merge(self, feed):
        if not feed:
            raise RuntimeError("Invalid parameter!")
        #  Loop through all the object's attributes.
        for attr, value in self.__dict__.items():
            #  If the object doesn't have a value for this attribute AND the object passed in DOES have a value, ...
            if not self.__dict__[attr] and feed.__dict__[attr]:
                #  Set it for this object.
                self.__dict__[attr] = feed.__dict__[attr]
