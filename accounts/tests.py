# accounts/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.profile = UserProfile.objects.create(user=self.user, name='Test User', email='testuser@example.com')

    def test_user_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.name, 'Test User')
        self.assertEqual(self.profile.email, 'testuser@example.com')
