import unittest
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestManufacturers(TestBase):
    def test_manufacturer(self):
        manufacturers = [b'Audi', b'BMW', b'Porsche', b'Ford', b'Ferrari', b'Lamborghini', b'Toyota']
        response = self.client.get(url_for('manufacturer'))
        self.assertIn(response.data, manufacturers)