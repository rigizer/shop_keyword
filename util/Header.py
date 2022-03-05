class Header:
    def __init__(self):
        self.header = None

    def make(self):
        self.header = {}

    def get_header(self):
        return self.header

    def set_header(self, header):
        self.header = header

    def add_header(self, header):
        pass