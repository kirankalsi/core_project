from flask import Flask, Response, request
import random

from application import app

@app.route('/manufacturer', methods=['GET'])
def manufacturer():
    manufacturers = ['Audi', 'BMW', 'Porsche', 'Ford', 'Ferrari', 'Lamborghini', 'Toyota']
    manufacturer = random.choice(manufacturers)
    return Response(manufacturer, mimetype='text/plain')