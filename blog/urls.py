from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('my-posts/', views.my_blog_posts, name='my_blog_posts'),
    path('blogs/', views.blog_posts, name='blog_posts'),
    path('blogs/category/<int:category_id>/',
         views.blog_posts_by_category, name='blog_posts_by_category'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
