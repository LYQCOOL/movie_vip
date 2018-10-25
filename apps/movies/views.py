from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


from .models import Movie_Detail
from .serializers import MovieSerializer

class MoviePagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class MovieView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    '''
    list:
        列出所有电影
    retrieve:
        进入电影
    '''
    queryset = Movie_Detail.objects.all()
    serializer_class = MovieSerializer
    # 分页
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    pagination_class = MoviePagination
    search_fields=('name','actors','decs')
