from django.contrib import admin
from django.urls import path
from . import views
from .views import blog_post_list, blog_post_detail
from .views import (
    PostUpdateView)


urlpatterns = [
    #path('', views.main, name='main'),
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
    path('create-blog-post/', views.create_blog_post, name='create_blog_post'),
    path('blog/', views.blog_post_list, name='blog_post_list'),
    path('blog/<int:post_id>/', views.blog_post_detail, name='blog_post_detail'),
    path('blog_detail/<int:post_id>/', views.blog_post_main, name='blog_post_main'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),

]
    
    
       

