class Post:
    def __init__(self):
        self.url = None

    def get_url(self):
        return self.url
    
    def set_url(self, url):
        self.url = url