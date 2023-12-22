from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from blog.serializers import ArticleListSerializer
from blog.models import Article


class ArticleList(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

    filter_backends = [DjangoFilterBackend]
    # 模糊筛选
    search_fields = ['title']
    # filterset_fields = ['title', 'update_time'] 精确筛选



class ArticleDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

"""class ArticleDetailSerializer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer"""





