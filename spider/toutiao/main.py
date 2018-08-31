#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author: wang
# Date: 18/08/16 11:36

from scrapy.cmdline import execute

import sys,os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","toutiao_news"])