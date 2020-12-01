import unittest
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestVehiclesTypes(TestBase):
    def test_vehicle_type(self):
        vehicle_types = [b'Hatchback', b'Roadster', b'Pickup Truck', b'Sports Car', b'Saloon', b'Convertible', b'Hybrid']
        response = self.client.get(url_for('vehicle_type'))
        self.assertIn(response.data, vehicle_types)