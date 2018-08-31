from django.db import models


# Create your models here.


class CctvWorldInfo(models.Model):
    news_id = models.CharField(max_length=50, default=0, verbose_name='新闻ID')
    url = models.CharField(max_length=500, default='', verbose_name='地址链接')
    front_image_url = models.CharField(max_length=500, default='', verbose_name='列表图片地址', blank=True, null=True)
    content_image_url = models.CharField(max_length=500, default='', verbose_name='内容图片地址', blank=True, null=True)
    title = models.CharField(max_length=200, default='', verbose_name='标题')
    summary = models.TextField(verbose_name='简介', default='')
    label = models.CharField(max_length=50, default='', verbose_name='标签')
    from_news = models.CharField(max_length=50, default='CCTV', verbose_name='来源')
    content = models.TextField(verbose_name='内容', default='')
    release_time = models.CharField(max_length=200, default='0000-00-00 00:00:00')
    create_date = models.DateTimeField(auto_now=True, verbose_name="创建时间")


class TouTiaoNewsInfo(models.Model):
    news_id = models.CharField(max_length=50, default=0, verbose_name='新闻ID')
    url = models.CharField(max_length=500, default='', verbose_name='地址链接')
    front_image_url = models.CharField(max_length=500, default='', verbose_name='列表图片地址', blank=True, null=True)
    content_image_url = models.CharField(max_length=500, default='', verbose_name='内容图片地址', blank=True, null=True)
    title = models.CharField(max_length=200, default='', verbose_name='标题')
    label = models.CharField(max_length=50, default='', verbose_name='标签')
    from_news = models.CharField(max_length=50, default='', verbose_name='来源')
    content = models.TextField(verbose_name='内容', default='')
    comment = models.IntegerField(verbose_name='评论数', default=0)
    release_time = models.CharField(max_length=200, default='0000-00-00 00:00:00')
    create_date = models.DateTimeField(auto_now=True, verbose_name="创建时间")
