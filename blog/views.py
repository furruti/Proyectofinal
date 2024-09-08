# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm  # Asegúrate de tener un formulario para crear/editar blogs

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})

def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/update_blog.html', {'form': form})

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'blog/delete_blog.html', {'blog': blog})
