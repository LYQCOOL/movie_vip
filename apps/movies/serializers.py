# _*_ encoding:utf-8 _*_
__author__ = 'LYQ'
__date__ = '2018/10/22 11:29'
from rest_framework import serializers
from .models import Movie_Detail


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_Detail
        fields = ('__all__')
