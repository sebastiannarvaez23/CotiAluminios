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
        self.common_user.set_password('passtest1')
        self.common_user.save()
        response = self.client.login(username=self.common_user.username, password='passtest1')
        self.assertEqual(response, True)

    def test_login_fail(self):
        self.common_user.set_password('passtest1')
        self.common_user.save()
        response = self.client.login(username=self.common_user.username, password='passtest2')
        self.assertEqual(response, False)

    def test_user_list(self):
        self.superuser.set_password('passtest1')
        self.superuser.save()
        self.client.login(username=self.superuser.username, password='passtest1')
        response = self.client.get('/auth/users/', HTTP_X_REQUEST_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)

    def test_user_list_without_auth(self):
        response = self.client.get('/auth/users/', HTTP_X_REQUEST_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 302)