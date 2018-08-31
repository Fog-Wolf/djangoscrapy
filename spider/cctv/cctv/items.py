# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy_djangoitem import DjangoItem
from spider.models import CctvWorldInfo
from scrapy.loader.processors import MapCompose, TakeFirst, Join, Identity


class CctvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CctvWorldItemLoader(ItemLoader):
    # 自定义itemLoader
    # default_output_processor = TakeFirst()
    pass


class CctvWorldItem(DjangoItem):
    django_model = CctvWorldInfo
