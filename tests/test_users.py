from django.test import TestCase, Client
from .factories import (
    UserCommonFactory,
    UserSuperuserFactory,
    UserStaffFactory
)

class UserTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.common_user = UserCommonFactory.create()
        self.superuser = UserSuperuserFactory.create()
        self.staff_user = UserStaffFactory.create()

    def test_common_user_creation(self):
        self.assertEqual(self.common_user.is_active, True)
        self.assertEqual(self.common_user.is_staff, False)
        self.assertEqual(self.common_user.is_superuser, False)

    def test_staff_user_creation(self):
        self.assertEqual(self.staff_user.is_active, True)
        self.assertEqual(self.staff_user.is_staff, True)
        self.assertEqual(self.staff_user.is_superuser, False)

    def test_superuser_creation(self):
        self.assertEqual(self.superuser.is_active, True)
        self.assertEqual(self.superuser.is_staff, True)
        self.assertEqual(self.superuser.is_superuser, True)

    def test_user_login(self):
        response = self.client.login(username=self.common_user.username, password=self.common_user.password)
        print(response)