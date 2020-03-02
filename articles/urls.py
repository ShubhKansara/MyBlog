from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article-list'),
    path('(?P<slug>[w-]+)/', views.article_details, name='articles-details'),

] 