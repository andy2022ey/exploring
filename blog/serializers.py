from rest_framework import serializers
from blog.models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='blog:detail')
    class Meta:
        model = Article
        fields = ['url', 'title', 'extract', 'update_time']


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'