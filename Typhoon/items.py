# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class TyphoonItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    author = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    content = scrapy.Field()
    keywords = scrapy.Field()
    datetime = scrapy.Field()

class UDNItem(TyphoonItem):
    # define the fields for your item here like:
    pass

class CHTItem(TyphoonItem):
    # define the fields for your item here like:
    pass