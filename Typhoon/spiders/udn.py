# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import XPathSelector
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup

class UdnSpider(CrawlSpider):
    name = 'udn'
    allowed_domains = ['udn.com']
    start_urls = ['https://www.google.com.tw/search?q=%E9%A2%B1%E9%A2%A8+site%3Audn.com&source=lnt&tbs=cdr%3A1%2Ccd_min%3A1%2F1%2F2018%2Ccd_max%3A10%2F31%2F2018&tbm=',
    'https://www.google.com.tw/search?tbs=cdr%3A1%2Ccd_min%3A1%2F1%2F2018%2Ccd_max%3A10%2F31%2F2018&ei=8ygeXZLDNIymmAW18Ku4Cw&q=%E7%91%AA%E8%8E%89%E4%BA%9E%E9%A2%B1%E9%A2%A8+site%3Audn.com&oq=%E7%91%AA%E8%8E%89%E4%BA%9E%E9%A2%B1%E9%A2%A8+site%3Audn.com&gs_l=psy-ab.3...21676.26091..27101...2.0..0.143.1047.15j1......0....1..gws-wiz.HCr4pTl0vFg']
    rules = [
        Rule(LinkExtractor(allow='https://udn.com/news/.*'),
             callback='parse', follow=True),
    ]
    def parse(self, response):
        item = UDNItem()
        # soup = BeautifulSoup(response.text, 'lxml')
        
        item['url'] = response.url
        item['title'] = response.xpath('//*[@id="story_art_title"]/text()').get()
        item['datetime'] = response.xpath('//*[@id="story_bady_info"]/div/span/text()').get()
        item['category'] = response.xpath('//*[@id="scroller"]/dl/dt[14]/a/text()').get()   
        divs = response.xpath('//*[@id="story_body_content"]')
        c = ''.join([p.get() for p in divs.xpath('p')]) 
        item['content'] 