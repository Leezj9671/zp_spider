import time
import random

import requests
from bs4 import BeautifulSoup

from . import headers
from . import config


class SpiderMeta(type):
    """
    爬虫元类，定义一些共用的方法
    """
    spiders = []

    def _init(cls):
        pass

    def __new__(cls, *args, **kwargs):

        args[2]['__init__'] = lambda self: SpiderMeta._init(self)
        args[2]['save_to_db'] = lambda self, ip_list: SpiderMeta._save_to_db(self, ip_list)
        args[2]['get_html'] = lambda self, url, use_proxy: SpiderMeta._get_html(self, url, use_proxy)

        SpiderMeta.spiders.append(type.__new__(cls, *args, **kwargs))
        return type.__new__(cls, *args, **kwargs)

    def _save_to_db(cls, data):
        

    def _get_html(cls, url, use_proxy):
        """
        解析html
        Args:
            url: str类型,解析页面的url
            use_agent: bool类型,是否使用代理

        Retruns:
            返回 BeautifulSoup 对象供解析
        """
        if use_proxy:
            proxies = { "http": requests.get(config.PROXY_API_URL).text }
        else:
            proxies = {}
        req_html = requests.get(url, headers=random.choice(headers.headers), proxies=proxies)
        try:
            soup = BeautifulSoup(req_html.content.decode("utf-8"), 'lxml')
        except UnicodeDecodeError:
            soup = BeautifulSoup(req_html.text, 'lxml')
        return soup


class LagouSpider(metaclass=SpiderMeta):
    """
    拉勾网爬虫
    """
    self.header = headers.lagou_header

    def crawl(self):

