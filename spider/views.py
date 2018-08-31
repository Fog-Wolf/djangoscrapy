from django.shortcuts import render
import hashlib
import re


# Create your views here.
def get_md5(url):
    # 判断参数是否为unicode
    if isinstance(url, str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


def clean_tag(value):
    # 去除数据中的特殊字符
    content = ""
    if type(value) == list:
        for con in value:
            line = re.sub('[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+', "", con)
            content += line
        return content
    else:
        return value

