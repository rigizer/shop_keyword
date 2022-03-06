from util.Result import Result
from util.Header import Header
from util.Post import Post

from taskJob.keywordmaster.KeywordmasterCV import KeywordmasterCV

from bs4 import BeautifulSoup

import datetime
import codecs
import time
import json
import os

import requests     # pip3 install requests

import util.Util as util

class Keywordmaster:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    @classmethod
    def make(cls, db_info):
        c = cls(db_info)
        return c

    def request_data(self, request_body):
        post = Post()
        post.set_url(KeywordmasterCV.INIT_URL)
        post.set_encoding(KeywordmasterCV.ENCODING)
        post.set_request_body(request_body)

        header = Header()
        header.set_header(KeywordmasterCV.HEADER_INFO)

        r = Result(None, post, header)
        r.send_request()

        return r

    def get_rate(self, rate):
        return rate.replace('<span style="font-size:12px;color:#666;">', '').replace('</span>', '')

    def parse_data(self, content):
        json_object = json.loads(content)

        keyword = util.replace_comma(json_object.get('name'))
        pc_search = util.replace_comma(json_object.get('pc'))
        mobile_search = util.replace_comma(json_object.get('mo'))
        total_view = util.replace_comma(json_object.get('sum'))
        doc_count = util.replace_comma(json_object.get('post'))
        rate = util.replace_comma(self.get_rate(json_object.get('byul')))

        data = {}
        data['keyword'] = keyword
        data['pc_search'] = int(pc_search)
        data['mobile_search'] = int(mobile_search)
        data['total_view'] = int(total_view)
        data['doc_count'] = int(doc_count)
        data['rate'] = float(rate)

        return data

    def insert_mws_keyword_rate(self, data):
        collect_site = data.get('collect_site')
        keyword = data.get('keyword')
        pc_search = data.get('pc_search')
        mobile_search = data.get('mobile_search')
        total_view = data.get('total_view')
        doc_count = data.get('doc_count')
        rate = data.get('rate')

        param = (
            collect_site, 
            keyword, 
            pc_search, 
            mobile_search, 
            total_view, 
            doc_count, 
            rate
        )

        self.db_handler.insert_mws_keyword_rate(param)

    def run(self, dataWithCollectsite):
        data = dataWithCollectsite.get_data()
        collect_site = dataWithCollectsite.get_collect_site()

        for rank in data.keys():
            keyword = data.get(rank)

            request_body = {
                'query': keyword, 
                's': True, 
                'queries': ''
            }

            result = self.request_data(request_body)
            content = result.get_content()
            p_data = self.parse_data(content)
            p_data['collect_site'] = collect_site

            self.insert_mws_keyword_rate(p_data)

            util.sleep(1.5)