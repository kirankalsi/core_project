from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestPrice(TestBase):
    def test_total_price_audi_hatchback(self):
        response=self.client.post('/total_price', json={'manufacturer': 'Audi', 'vehicle_type': 'Hatchback'})
        self.assertIn(b'45499', response.data)

    def test_total_price_bmw_roadster(self):
        response=self.client.post('/total_price', json={'manufacturer': 'BMW', 'vehicle_type': 'Roadster'})
        self.assertIn(b'57050', response.data)

    def test_total_price_porsche_pickup_truck(self):
        response=self.client.post('/total_price', json={'manufacturer': 'Porsche', 'vehicle_type': 'Pickup Truck'})
        self.assertIn(b'107888', response.data)

    def test_total_price_ford_sports_car(self):
        response=self.client.post('/total_price', json={'manufacturer': 'Ford', 'vehicle_type': 'Sports Car'})
        self.assertIn(b'31500', response.data)

    def test_total_price_ferrari_saloon(self):
        response=self.client.post('/total_price', json={'manufacturer': 'Ferrari', 'vehicle_type': 'Saloon'})
        self.assertIn(b'163333', response.data)

    def test_total_price_lamborghini_convertible(self):
        response=self.client.post('/total_price', json={'manufacturer': 'Lamborghini', 'vehicle_type': 'Convertible'})
        self.assertIn(b'171500', response.data)

    def test_total_price_toyota_supermini(self):
        response=self.client.post('/total_price', json={'manufacturer': 'Toyota', 'vehicle_type': 'Supermini'})
        self.assertIn(b'36499', response.data)



'''    
    def test_man_price_audi(self):
        response = self.client.post(
            url_for('total_price'),
            data='Audi',
            follow_redirects=True
        )
        self.assertIn(b'45499' or '56550' or '53388' or '64500' or '47833' or '66000' or '54499', response.data)

'''
