# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import XPathSelector
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup

from Typhoon.items import UDNItem

class UdnSpider(CrawlSpider):
    name = 'udn'
    allowed_domains = ['udn.com']
    start_urls = ['https://www.google.com.tw/search?q=%E9%A2%B1%E9%A2%A8+site:udn.com&tbs=cdr:1,cd_min:1/1/2018,cd_max:10/31/2018&ei=SAgfXfAboYqvvA-JrZKYBw&start=0&sa=N&ved=0ahUKEwjw3_KgrJ3jAhUhxYsBHYmWBHM4ChDy0wMIfg&biw=1440&bih=716&num=200',]
    # rules = [
    Rule(LinkExtractor(allow=('https://www.google.com.tw/search?q=%E9%A2%B1%E9%A2%A8+site:udn.com&tbs=cdr:1,cd_min:1/1/2018,cd_max:10/31/2018&.*')),  # 'https://www.google.com.tw/.*'
         callback='parse', follow=True)
    # ]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        articles = soup.find_all(
            'a', href=re.compile('.*https://udn.com/news.*'))

        for article_url in articles:
            m = re.search('=(.+?)&', article_url['href'])
            if m:
                url = m.group(1)
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        item = UDNItem()
        # soup = BeautifulSoup(response.text, 'lxml')

        item['url'] = response.url
        item['title'] = response.xpath(
            '//*[@id="story_art_title"]/text()').get()
        item['datetime'] = response.xpath(
            '//*[@id="story_bady_info"]/div/span/text()').get()
        item['author'] = response.xpath(
            '//*[@id="story_bady_info"]/div/a/text()').get()
        item['category'] = response.xpath(
            '//*[@id="scroller"]/dl/dt[14]/a/text()').get()
        divs = response.xpath('//*[@id="story_body_content"]')
        c = ''.join([p.get() for p in divs.xpath('p')])
        item['content'] = ''.join([p.get() for p in divs.xpath('p/text()')])
        return item
