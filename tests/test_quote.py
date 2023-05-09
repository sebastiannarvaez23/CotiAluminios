import json

from django.test import TestCase, Client
from tests.factories.stylewindow import StyleWindowFactory
from tests.factories.aluminumfinishes import AluminumFinishesFactory
from tests.factories.glasstype import GlassTypeFactory
from tests.factories.quote import (
    MasterServiceGlassFrostedFactory,
    MasterArticleLockFactory,
    MasterArticleCornerFactory,
)

class QuoteTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.stylewindow = StyleWindowFactory.create()
        self.aluminumfinishes = AluminumFinishesFactory.create()
        self.glasstype = GlassTypeFactory.create()
        self.glassfrosted = MasterServiceGlassFrostedFactory.create()
        self.lock = MasterArticleLockFactory.create()
        self.corner = MasterArticleCornerFactory.create()

    def test_get_quote_window(self):
        data = {
            "window_width": 9,
            "window_height": 15,
            "window_style": 1,
            "aluminum_finishes": 1,
            "type_glass": 1,
            "glass_frosted": False,
            "num_window_quote": 1
        }
        response = self.client.post('/api/quote/', json.dumps(data), content_type='application/json', HTTP_X_REQUEST_WITH='XMLHttpRequest')
        response = response.json()
        self.assertEqual(response['status_code'], 200)
        self.assertEqual(response['result'], '$30,002.00')

        
        
