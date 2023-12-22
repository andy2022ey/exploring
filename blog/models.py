from django.db import models
from django.utils import timezone


class Category(models.Model):
    # 分类
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-create_time']


class Article(models.Model):
    title = models.CharField(max_length=100)  # 文章标题
    extract = models.TextField(blank=True, null=True)  # 文章摘要
    create_time = models.DateTimeField(default=timezone.now)  # 创建时间
    update_time = models.DateTimeField(auto_now=True)  # 修改时间
    content = models.TextField(blank=True, null=True)  # 文章内容
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True,related_name='articles')

    def __str__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-update_time']



