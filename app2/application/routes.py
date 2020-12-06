from flask import Flask, Response, request
import random

from application import app

@app.route('/manufacturer', methods=['GET'])
def manufacturer():
    manufacturers = ['AUDI', 'BMW', 'PORSCHE', 'FORD', 'FERRARI', 'LAMBORGHINI', 'TOYOTA']
    manufacturer = random.choice(manufacturers)
    return Response(manufacturer, mimetype='text/plain')