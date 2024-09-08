from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Blog

class BlogModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.blog = Blog.objects.create(
            title='Título de prueba',
            subtitle='Subtítulo de prueba',
            body='Este es el cuerpo del blog de prueba.',
            author=self.user,
        )

    def test_blog_content(self):
        self.assertEqual(self.blog.title, 'Título de prueba')
        self.assertEqual(self.blog.subtitle, 'Subtítulo de prueba')
        self.assertEqual(self.blog.body, 'Este es el cuerpo del blog de prueba.')
        self.assertEqual(self.blog.author.username, 'testuser')

class BlogViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.blog = Blog.objects.create(
            title='Título de prueba',
            subtitle='Subtítulo de prueba',
            body='Este es el cuerpo del blog de prueba.',
            author=self.user,
        )

    def test_blog_list_view(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Título de prueba')
        self.assertTemplateUsed(response, 'blog/blog_list.html')

    def test_blog_detail_view(self):
        response = self.client.get(reverse('blog_detail', args=[self.blog.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.blog.title)
        self.assertTemplateUsed(response, 'blog/blog_detail.html')

    def test_create_blog_view(self):
        response = self.client.post(reverse('create_blog'), {
            'title': 'Nuevo blog',
            'subtitle': 'Nuevo subtítulo',
            'body': 'Contenido del nuevo blog',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)  # Redirección tras la creación
        self.assertEqual(Blog.objects.last().title, 'Nuevo blog')

    def test_update_blog_view(self):
        response = self.client.post(reverse('update_blog', args=[self.blog.id]), {
            'title': 'Título actualizado',
            'subtitle': 'Subtítulo actualizado',
            'body': 'Contenido actualizado'
        })
        self.assertEqual(response.status_code, 302)  # Redirección tras la actualización
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.title, 'Título actualizado')

    def test_delete_blog_view(self):
        response = self.client.post(reverse('delete_blog', args=[self.blog.id]))
        self.assertEqual(response.status_code, 302)  # Redirección tras la eliminación
        self.assertFalse(Blog.objects.filter(id=self.blog.id).exists())
