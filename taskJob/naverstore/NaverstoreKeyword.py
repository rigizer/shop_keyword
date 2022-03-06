from util.Result import Result
from util.Header import Header
from util.Post import Post
from util.DataWithCollectsite import DataWithCollectsite

from taskJob.naverstore.NaverstoreCV import NaverstoreCV

from bs4 import BeautifulSoup

import datetime
import time
import json
import os

import requests     # pip3 install requests

class NaverstoreKeyword:
    def __init__(self, db_handler):
        self.db_handler = db_handler
        self.collect_site = 'shopping.naver.com'

    @classmethod
    def make(cls, db_info):
        c = cls(db_info)
        return c

    def request_data(self, request_body):
        post = Post()
        post.set_url(NaverstoreCV.INIT_URL)
        post.set_request_body(request_body)
        post.set_datatype('JSON')

        header = Header()
        header.set_header(NaverstoreCV.HEADER_INFO)

        r = Result(None, post, header)
        r.send_request()
        content = r.get_content()

        return content

    def parse_data(self, content):
        json_object = json.loads(content)
        items = json_object.get('data').get('KeywordChartList').get('charts')

        data = {}

        for item in items:
            rank = item.get('rank')
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
        request_body = {
            'query': 'query ChartList($params: ChartListInput) {KeywordChartList(params: $params) { rankedDate period demo categoryId charts {rank change brandSeq brandName exposeBrandName keyword exposeKeyword rankedReason}}}', 
            'variables': {
                'params': {
                    'categoryId': 'ALL', 
                    'demo': 'A00', 
                    'period': 'P1D', 
                    'rankStart': 1, 
                    'rankEnd': 20
                }
            }
        }

        content = self.request_data(request_body)
        data = self.parse_data(content)
        self.insert_mws_keyword(data)

        dataWithCollectsite = DataWithCollectsite()
        dataWithCollectsite.set_data(data)
        dataWithCollectsite.set_collect_site(self.collect_site)

        return dataWithCollectsite