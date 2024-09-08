from django.urls import path
from .views import blog_list, blog_detail, create_blog, update_blog, delete_blog, about

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('about/', about, name='about'),
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('blog/new/', create_blog, name='create_blog'),
    path('blog/<int:blog_id>/edit/', update_blog, name='update_blog'),
    path('blog/<int:blog_id>/delete/', delete_blog, name='delete_blog'),
]
