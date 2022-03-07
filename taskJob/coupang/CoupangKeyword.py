from util.Result import Result
from util.Header import Header
from util.Get import Get
from util.DataWithCollectsite import DataWithCollectsite

from taskJob.coupang.CoupangCV import CoupangCV

from bs4 import BeautifulSoup

import datetime
import time
import json
import os

import requests     # pip3 install requests

class CoupangKeyword:
    def __init__(self, db_handler):
        self.db_handler = db_handler
        self.collect_site = 'coupang.com'

    @classmethod
    def make(cls, db_info):
        c = cls(db_info)
        return c

    def request_data(self):
        get = Get()
        get.set_url(CoupangCV.INIT_URL)

        header = Header()
        header.set_header(CoupangCV.HEADER_INFO)

        r = Result(get, None, header)
        r.send_request()
        content = r.get_content()

        return content

    def parse_data(self, content):
        json_object = json.loads(content)
        items = json_object.get('rData').get('entityList')[0].get('entity').get('links')

        data = {}

        for item in items:
            rank = int(item.get('subNameAttr')[0].get('text'))
            keyword = item.get('nameAttr')[0].get('text')

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

        dataWithCollectsite = DataWithCollectsite()
        dataWithCollectsite.set_data(data)
        dataWithCollectsite.set_collect_site(self.collect_site)

        return dataWithCollectsite