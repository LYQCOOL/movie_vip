# _*_ encoding:utf-8 _*_
__author__ = 'LYQ'
__date__ = '2018/10/17 9:33'
import xadmin
from .models import *


class MovieAdmin(object):
    list_display = ['name', 'url', 'score', 'actors', 'decs', 'bofang_nums', 'movie_img_url']
    search_fields = ['name', 'actors']


xadmin.site.register(Movie_Detail, MovieAdmin)
