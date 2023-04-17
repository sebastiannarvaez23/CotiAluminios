from django.test import TestCase
from faker import Faker
from .factories import user_factory

fake = Faker()

class UserTestCase(TestCase):

    def setUp(self):
        self.user = user_factory()
    
    def test_user_creation(self):
        self.user.save()
        self.assertEqual(self.user.is_active, True)
        self.assertEqual(self.user.is_staff, False)
        self.assertEqual(self.user.is_superuser, False)

    def test_staff_user_creation(self):
        self.user.is_staff = True
        self.user.save()
        assert self.user.is_staff

    def test_superuser_creation(self):
        self.user.is_superuser = True
        self.user.is_staff = True
        self.user.save()
        assert self.user.is_superuser
