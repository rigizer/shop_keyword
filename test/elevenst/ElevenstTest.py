class ElevenstKeyword:
    def __init__(self):
        pass

    @classmethod
    def make(cls):
        c = cls()
        return c

    def request_data(self):
        get = Get()
        get.set_url(ElevenstCV.INIT_URL)

        header = Header()
        header.set_header(ElevenstCV.HEADER_INFO)

        r = Result(get, None, header)
        r.send_request()
        content = r.get_content()

        return content

    def parse_data(self, content):
        soup = BeautifulSoup(content, 'html.parser')


    def run(self):
        content = self.request_data()
        #data = self.parse_data(content)

        print(content)

def main():
    c = ElevenstKeyword.make()
    c.run()

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ))

        from util.Result import Result
        from util.Header import Header
        from util.Get import Get

    else:
        from ...util.Result import Result
        from ...util.Header import Header
        from ...util.Get import Get

    from ElevenstCV import ElevenstCV

    from bs4 import BeautifulSoup

    import datetime
    import time
    import json
    import os

    import requests     # pip3 install requests

    main()