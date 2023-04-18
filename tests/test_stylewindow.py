from django.test import TestCase, Client
from .factories import (
    UserCommonFactory,
    UserSuperuserFactory,
    UserStaffFactory
)

class StyleWindowTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.common_user = UserCommonFactory.create()
        self.superuser = UserSuperuserFactory.create()
        self.staff_user = UserStaffFactory.create()
    
    def test_window_style_page(self):
        self.common_user.set_password('passtest1')
        self.common_user.save()
        self.client.login(username=self.common_user.username, password='passtest1')
        response = self.client.get('/window/styles/', HTTP_X_REQUEST_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
    
    def test_window_style_create(self):
        data_form = {
            'name': 'nametest1',
            'price': '1'
        }
        self.common_user.set_password('passtest1')
        self.common_user.save()
        self.client.login(username=self.common_user.username, password='passtest1')
        response = self.client.post('/window/styles/create', data=data_form, HTTP_X_REQUEST_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 301)
    
    def test_window_style_create_fail(self):
        data_form = {
            'price': 'nametest1',
        }
        self.common_user.set_password('passtest1')
        self.common_user.save()
        self.client.login(username=self.common_user.username, password='passtest1')
        response = self.client.post('/window/styles/create', data=data_form, HTTP_X_REQUEST_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 400)
