# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from Typhoon.items import CHTItem

class ChinatimesSpider(CrawlSpider):
    name = 'cht_maria'
    allowed_domains = ['www.chinatimes.com']
    start_urls = ['https://www.google.com.tw/search?q=%E7%91%AA%E8%8E%89%E4%BA%9E%E9%A2%B1%E9%A2%A8+site:www.chinatimes.com&tbs=cdr:1,cd_min:1/1/2018,cd_max:10/31/2018&ei=yvQeXaGWKor48QXclKSQAQ&start=70&sa=N&ved=0ahUKEwiho-fVmZ3jAhUKfLwKHVwKCRI4UBDx0wMIdA&biw=1440&bih=716']
    rules = [
        Rule(LinkExtractor(allow='https://www.google.com.tw/.*'),
             callback='parse', follow=True),
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        articles = soup.find_all('a', href=re.compile('.*https://www.chinatimes.com/.*'))
        
        for article_url in articles:
            m = re.search('=(.+?)&', article_url['href'])
            if m:
                url = m.group(1)
            yield scrapy.Request(url+'?chdtv', callback=self.parse_item)

    def parse_item(self, response):
        item = CHTItem()

        item['url'] = response.url
        item['title'] = response.xpath('//*[@id="page-top"]/div/div[2]/div/div/article/div/header/h1/text()').get()
        item['author'] = response.xpath('//*[@id="page-top"]/div/div[2]/div/div/article/div/header/div/div[1]/div/div/div[2]/a/text()').get()
        item['datetime'] = response.xpath('//*[@id="page-top"]/div/div[2]/div/div/article/div/header/div/div[1]/div/div/time/span[2]/text()').get() \
        +' '+response.xpath('//*[@id="page-top"]/div/div[2]/div/div/article/div/header/div/div[1]/div/div/time/span[1]/text()').get()
        item['category'] = response.xpath('//*[@id="page-top"]/div/div[1]/nav/ol/li[2]/a/span/text()').get()   

        divs = response.xpath('//*[@id="page-top"]/div/div[2]/div/div/article/div/div[1]/div[2]/div[2]/div[2]')
        c = ''.join([p.get() for p in divs.xpath('p')]) 
        item['content'] = ''.join([p.get() for p in divs.xpath('p/text()')])
        return item
