import os
import json

import requests     # pip3 install requests

class Result:
    def __init__(self, get, post, header):
        if get != None:
            self.url = get.get_url()
        
        if post != None:
            self.url = post.get_url()
        
        self.header = header.get_header()

        self.content = None
        self.status_code = None

    def send_request(self):
        url = self.url
        header = self.header

        response = requests.get(url, params=header)
        self.content = response.text
        self.status_code = response.status_code

    def get_content(self):
        return self.content

    def get_status_code(self):
        return self.status_code