from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestManufacturerPrice(TestBase):
    def test_man_price_audi(self):
        response = self.client.post(
            url_for('total_price'),
            data='Audi',
            follow_redirects=True
        )
        self.assertIn(b'45499' or '56550' or '53388' or '64500' or '47833' or '66000' or '54499', response.data)
'''
    def test_man_price_audi(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "Audi"
                p.return_value.text = 44500

                response = self.client.get(url_for('total_price'))
                self.assertIn(b'Audi', response.data)
                #self.assertIn(b'12', response.data)
                #self.assertEqual(response.status_code, 200)
'''
