import os
import json
from turtle import end_fill

import requests     # pip3 install requests

class Result:
    def __init__(self, get, post, header):
        self.request_body = None

        if get != None:
            self.type = 'GET'
            self.url = get.get_url()
            self.encoding = get.get_encoding()
        
        if post != None:
            self.type = 'POST'
            self.url = post.get_url()
            self.encoding = post.get_encoding()
            
            if post.get_request_body() != None:
                self.request_body = post.get_request_body()
        
        self.header = header.get_header()

        self.content = None
        self.status_code = None

    def send_request(self):
        url = self.url
        header = self.header
        encoding = self.encoding
        request_body = self.request_body

        if self.type == 'GET':
            response = requests.get(url, headers=header)
            response.encoding = encoding
        if self.type == 'POST':
            response = requests.post(url, headers=header, data=request_body)
            response.encoding = encoding

        self.content = response.text
        self.status_code = response.status_code

    def get_content(self):
        return self.content

    def get_status_code(self):
        return self.status_code

    def get_type(self):
        return self.type