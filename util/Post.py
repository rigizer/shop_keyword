class Post:
    def __init__(self):
        self.url = None
        self.encoding = 'utf-8'
        self.request_body = None
        self.datatype = None

    def get_url(self):
        return self.url
    
    def set_url(self, url):
        self.url = url

    def get_encoding(self):
        return self.encoding

    def set_encoding(self, encoding):
        self.encoding = encoding

    def get_request_body(self):
        return self.request_body

    def set_request_body(self, request_body):
        self.request_body = request_body

    def get_datatype(self):
        return self.datatype

    def set_datatype(self, datatype):
        self.datatype = datatype