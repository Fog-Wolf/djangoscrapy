# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.http import request
from urllib import parse
from spider.cctv.cctv.items import CctvWorldItem
from spider.views import get_md5,clean_tag
import datetime

class NewsWorldSpider(scrapy.Spider):
    name = 'news_world'
    allowed_domains = ['http://news.cctv.com']
    start_urls = ['http://news.cctv.com/world/']

    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

    headers = {
        "HOST": "news.cctv.com",
        "Referer": "http://news.cctv.com/world/",
        "User-Agent": agent
    }

    def __init__(self):
        self.brower = webdriver.Chrome(executable_path="D:/python/chromedriver.exe")
        super(NewsWorldSpider, self).__init__()

    def parse(self, response):
        # 解析列表页
        url_nodes = response.css(".col_w660 .main #leftContent .ecoA9805_con02 ")
        for url in url_nodes:
            post_url = url.css("h3 .l a::attr(href)").extract_first()
            title = url.css("h3 .l a::text").extract_first()
            image_url = url.css(".text_box .l a img::attr(src)").extract_first()
            summary = url.css(".text_box p::text").extract_first()
            label = url.css(".text_box h4 a::text").extract()
            release_time = url.css(".text_box h5 i::text").extract_first()
            print(post_url)
            yield request.Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail,
                                  meta={'front_image_url': image_url, "title": title, "summary": summary,
                                        'label': label, 'release_time': release_time}, headers=self.headers,
                                  dont_filter=True)

    def parse_detail(self, response):
        world_info = CctvWorldItem()
        world_info['url'] = response.url
        world_info['news_id'] = get_md5(response.url)
        world_info['title'] = response.meta.get("title", "")
        world_info['from_news'] = response.css(".cnt_bd .function .info i a::text").extract_first("央视网")
        world_info['summary'] = response.meta.get("summary", "")
        world_info['label'] = ','.join(response.meta.get("label", ""))
        world_info['release_time'] = response.meta.get("release_time", "")
        world_info['front_image_url'] = response.meta.get("front_image_url", "")
        world_info['content_image_url'] = response.css("p img::attr(src)").extract_first()
        world_info['content'] = clean_tag(response.css(".cnt_bd p::text").extract())
        if world_info['content']== '请点此安装最新Flash' :
            world_info['content'] = response.xpath("/html/body/div[12]/div[1]/div[1]/p[4]/span/text()").extract_first()
            if world_info['content']:
                world_info['content'] = response.xpath("/html/body/div[12]/div[1]/div[1]/p[4]/span[2]/text()").extract_first()
        world_info['create_date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        world_info.save()

        yield scrapy.Request(response.url, callback=self.parse, headers=self.headers)
