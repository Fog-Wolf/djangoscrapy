# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from spider.models import TouTiaoNewsInfo
from scrapy_djangoitem import DjangoItem

class ToutiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ToutiaoNewsItem(DjangoItem):
    django_model = TouTiaoNewsInfo
