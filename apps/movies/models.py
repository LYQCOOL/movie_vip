from __future__ import unicode_literals

import datetime
from django.db import models


# Create your models here.

class Movie_Detail(models.Model):
    '''
    电影详情表
    '''
    name = models.CharField(max_length=100, verbose_name="电影名")
    url = models.CharField(max_length=300, verbose_name="电影链接")
    score = models.CharField(max_length=10, verbose_name="评分")
    actors = models.CharField(max_length=300, verbose_name="演员", null=True, blank=True)
    decs = models.CharField(max_length=200, verbose_name="电影描述")
    bofang_nums = models.CharField(max_length=20, verbose_name="播放量")
    movie_img_url = models.CharField(max_length=300, verbose_name="图片链接")
    create_time = models.DateTimeField(default=datetime.datetime.now(), verbose_name="创建时间")

    class Meta:
        verbose_name = "电影"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
