# _*_ encoding:utf-8 _*_
__author__ = 'LYQ'
__date__ = '2018/10/22 10:57'
import sys
import os


pwd=os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+'../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movies_vip.settings")

import django
django.setup()
#位置要放对，配置好引入
from movies.models import Movie_Detail
import MySQLdb
import datetime
conn=MySQLdb.Connect(host="localhost",user="root",passwd="112358",db="movies",charset='utf8')
cursor=conn.cursor()
cursor.execute("select * from movie_detail")
data=cursor.fetchall()
for da in data:
    # print(da)
    test=Movie_Detail()
    test.name=da[0]
    test.url=da[1]
    test.score=da[2]
    test.actors=da[3]
    test.decs=da[4]
    test.bofang_nums=da[5]
    test.movie_img_url=da[6]
    test.create_time=datetime.datetime.now()
    test.save()