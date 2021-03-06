from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Vehicles
from os import getenv

class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///',
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                DEBUG=True
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        
        db_info = Vehicles(manufacturer='Audi', vehicle_type='Sports Car', total_price='64500')
        db.session.add(db_info)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
'''
class TestViews(TestBase):

    def test_index_view(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
'''
class TestResponse(TestBase):
    def test_vehicle(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "Audi"
                #g.return_value.text = "Sports Car"
                p.return_value.text = "64500"

                response = self.client.get(url_for('index'))
                self.assertIn(b'Audi Audi', response.data)
                self.assertIn(b'The price is 64500 Pound Sterling', response.data)
                self.assertEqual(response.status_code, 200)