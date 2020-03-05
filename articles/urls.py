from django.urls import path, re_path
from . import views

app_name='article'
urlpatterns = [
    path('', views.article_list, name='article-list'),
    re_path(r'^(?P<slug>[\w-]+)/', views.article_details, name='articles-details'),

] 