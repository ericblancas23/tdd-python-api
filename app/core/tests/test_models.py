from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_sucessful(self):
        """Test creating new user with email is 200"""
        email = 'testemail@gmail.com'
        password = 'testpass123'
        user = get_user_model().objects.create(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
    def test_new_user_email_normalised(self):
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create(email, 'test123')

        self.assertEqual(user.email, email.lower())