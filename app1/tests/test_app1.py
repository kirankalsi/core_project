import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Vehicles
from os import getenv

class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                DEBUG=True
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        
        db_info = Vehicles(manufacturer='Audi', vehicle_type='Sports Car', total_price='50000')
        db.session.add(db_info)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)