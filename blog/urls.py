# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),  # Lista de blogs
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),  # Detalle de blog
    path('create/', views.create_blog, name='create_blog'),  # Crear blog
    path('<int:blog_id>/update/', views.update_blog, name='update_blog'),  # Actualizar blog
    path('<int:blog_id>/delete/', views.delete_blog, name='delete_blog'),  # Eliminar blog
]
