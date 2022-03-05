from util.Result import Result
from util.Header import Header
from util.Get import Get

from taskJob.elevenst.ElevenstCV import ElevenstCV

from bs4 import BeautifulSoup

import datetime
import time
import json
import os

import requests     # pip3 install requests

class ElevenstKeyword:
    def __init__(self, db_handler):
        self.db_handler = db_handler
        self.collect_site = '11st.co.kr'

    @classmethod
    def make(cls, db_info):
        c = cls(db_info)
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
        #soup = BeautifulSoup(content, 'html.parser')
        content = content.replace('fetchSearchRanking(', '')[:-1]
        
        json_object = json.loads(content)
        items = json_object.get('items')

        data = {}

        for item in items:
            rank = item.get('currentRank')
            keyword = item.get('keyword')

            data[rank] = keyword

        return data

    def insert_mws_keyword(self, data):
        collect_site = self.collect_site

        for rank in data.keys():
            keyword = data.get(rank)

            param = (
                collect_site, 
                keyword, 
                rank
            )

            self.db_handler.insert_mws_keyword(param)

    def run(self):
        content = self.request_data()
        data = self.parse_data(content)
        self.insert_mws_keyword(data)