class Get:
    def __init__(self):
        self.url = None
        self.encoding = 'utf-8'

    def get_url(self):
        return self.url
    
    def set_url(self, url):
        self.url = url

    def get_encoding(self):
        return self.encoding

    def set_encoding(self, encoding):
        self.encoding = encoding