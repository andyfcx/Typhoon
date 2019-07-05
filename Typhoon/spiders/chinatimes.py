# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup

class ChinatimesSpider(CrawlSpider):
    name = 'chinatimes'
    allowed_domains = ['www.chinatimes.com']
    start_urls = ['https://www.google.com.tw/search?tbs=cdr%3A1%2Ccd_min%3A1%2F1%2F2018%2Ccd_max%3A10%2F31%2F2018&ei=cykeXc6xLPOZr7wPk462qAg&q=%E9%A2%B1%E9%A2%A8+site%3Awww.chinatimes.com&oq=%E9%A2%B1%E9%A2%A8+site%3Awww.chinatimes.com&gs_l=psy-ab.3...18765.19081..20076...0.0..0.69.183.3......0....1..gws-wiz.HpQVPgoVw8c',
        'https://www.google.com.tw/search?tbs=cdr%3A1%2Ccd_min%3A1%2F1%2F2018%2Ccd_max%3A10%2F31%2F2018&ei=ECkeXdHdH46Tr7wP_rKgoAc&q=%E7%91%AA%E8%8E%89%E4%BA%9E%E9%A2%B1%E9%A2%A8+site%3Awww.chinatimes.com&oq=%E7%91%AA%E8%8E%89%E4%BA%9E%E9%A2%B1%E9%A2%A8+site%3Awww.chinatimes.com&gs_l=psy-ab.3...94783.94783..98581...0.0..0.143.143.0j1......0....2j1..gws-wiz.Ba4tp3I7VeI']
    rules = [
        Rule(LinkExtractor(allow='https://www.chinatimes.com/.*'),
             callback='parse_list', follow=True),
    ]
    def parse(self, response):
        pass
