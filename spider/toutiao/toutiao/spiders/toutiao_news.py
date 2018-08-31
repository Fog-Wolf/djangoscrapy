# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.http import request
from urllib import parse
from spider.toutiao.toutiao.items import ToutiaoNewsItem
from spider.views import get_md5


class ToutiaoNewsSpider(scrapy.Spider):
    name = 'toutiao_news'
    allowed_domains = ['https://www.toutiao.com']
    start_urls = ['https://www.toutiao.com/ch/news_hot/']

    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

    headers = {
        "HOST": "www.toutiao.com",
        "Referer": "https://www.toutiao.com/ch/news_hot/",
        "User-Agent": agent
    }

    def __init__(self):
        self.brower = webdriver.Chrome(executable_path="D:/python/chromedriver.exe")
        super(ToutiaoNewsSpider, self).__init__()

    def parse(self, response):
        url_nodes = response.css('.feedBox li')
        for url in url_nodes:
            post_url = url.css(".rbox-inner .title-box a::attr(href)").extract_first()
            title = url.css(".rbox-inner .title-box a::text").extract_first()
            front_image_url = url.css(".lbox .img-wrap img::attr(src)").extract_first()
            come_from_url = url.css(".footer .y-left .media-avatar::attr(href)").extract_first()
            come_from_name = url.css(".footer .y-left .source::text").extract_first()
            come_from_image_url = url.css(".footer .y-left .media-avatar img::attr(src)").extract_first()
            comment = url.css(".footer .y-left .comment::text").extract_first()
            print(post_url)
            yield request.Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail,
                                  meta={'front_image_url': front_image_url, "title": title,
                                        "come_from_url": come_from_url,
                                        'come_from_name': come_from_name, 'come_from_image_url': come_from_image_url,
                                        'comment': comment}, headers=self.headers,
                                  dont_filter=True)

    def parse_detail(self, response):
        tou_tiao = ToutiaoNewsItem()
        tou_tiao['url'] = response.url
        tou_tiao['news_id'] = get_md5(response.url)
        tou_tiao['title'] = response.meta.get("title", "")
        tou_tiao['front_image_url'] = response.meta.get("front_image_url", "")
        tou_tiao['come_from_url'] = response.meta.get("come_from_url", "")
        tou_tiao['come_from_name'] = response.meta.get("come_from_name", "")
        tou_tiao['come_from_image_url'] = response.meta.get("come_from_image_url", "")
        tou_tiao['comment'] = response.meta.get("comment", "")
        tou_tiao['content_image_url'] = response.css('.pgc-img img::attr(src)').extract()
        pass
