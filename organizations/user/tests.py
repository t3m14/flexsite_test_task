from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class UserModelTests(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'first_name': 'Test',
            'last_name': 'User'
        }

    def test_create_user_with_email_successful(self):
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.email, self.user_data['email'])
        self.assertTrue(user.check_password(self.user_data['password']))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_without_email_raises_error(self):
        self.user_data['email'] = ''
        with self.assertRaises(ValidationError):
            User.objects.create_user(**self.user_data)

    def test_create_superuser(self):
        user = User.objects.create_superuser(**self.user_data)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_email_normalized(self):
        email = 'test@EXAMPLE.com'
        self.user_data['email'] = email
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.email, email.lower())

    def test_invalid_email(self):
        self.user_data['email'] = 'notanemail'
        with self.assertRaises(ValidationError):
            user = User.objects.create_user(**self.user_data)
            user.full_clean()

    def test_create_user_with_long_email(self):
        self.user_data['email'] = 'a' * 245 + '@example.com'
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.email, self.user_data['email'])

    def test_create_user_with_no_first_name(self):
        self.user_data['first_name'] = ''
        with self.assertRaises(ValidationError):
            user = User.objects.create_user(**self.user_data)
            user.full_clean()
    def test_create_user_with_no_last_name(self):
        self.user_data['last_name'] = ''
        with self.assertRaises(ValidationError):
            user = User.objects.create_user(**self.user_data)
            user.full_clean()
    def test_create_user_with_no_password(self):
        self.user_data['password'] = ''
        with self.assertRaises(ValidationError):
            user = User.objects.create_user(**self.user_data)
            user.full_clean()
    def test_create_user_with_no_email(self):
        self.user_data['email'] = ''
        with self.assertRaises(ValidationError):
            user = User.objects.create_user(**self.user_data)
            user.full_clean()
    def test_create_user_with_invalid_email(self):
        self.user_data['email'] = 'notanemail'
        with self.assertRaises(ValidationError):
            user = User.objects.create_user(**self.user_data)
            user.full_clean()
    def test_create_user_with_long_email(self):
        self.user_data['email'] = 'a' * 245 + '@example.com'
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.email, self.user_data['email'])
    def test_create_user_with_long_first_name(self):
        self.user_data['first_name'] = 'a' * 151
        with self.assertRaises(ValidationError):
            user = User.objects.create_user(**self.user_data)
            user.full_clean()
    def test_create_user_with_long_last_name(self):
        self.user_data['last_name'] = 'a' * 151
        with self.assertRaises(ValidationError):
            user = User.objects.create_user(**self.user_data)
            user.full_clean()
    def test_create_user_with_long_password(self):
        self.user_data['password'] = 'a' * 129
        with self.assertRaises(ValidationError):
            user = User.objects.create_user(**self.user_data)
            user.full_clean()
    def test_create_user_with_invalid_email(self):
        self.user_data['email'] = 'notanemail'
        with self.assertRaises(ValidationError):
            user = User.objects.create_user(**self.user_data)
            user.full_clean()
