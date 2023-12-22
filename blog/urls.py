from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog import views


# 创建路由器并注册视图集
router = DefaultRouter()
router.register(r'article', views.ArticleList, basename='article')

app_name = 'blog'

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
]