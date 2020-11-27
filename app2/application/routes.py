from flask import Flask, Response, request, jsonify
import random

from application import app

@app.route('/manufacturer', methods=['GET'])
def manufacturer():
    manufacturers = ['Audi', 'BMW', 'Porsche', 'Ford', 'Ferrari', 'Lamborghini', 'Toyota']
    manufacturer = random.choice(manufacturers)
    return Response(manufacturer, mimetype='text/plain')

@app.route('/price', methods=['POST'])
def price():
    data_sent = request.data.decode('utf-8')
    if data_sent == 'Audi':
        price = 44500
    elif data_sent == 'BMW':
        price = 45000
    elif data_sent == 'Porsche':
        price = 99000
    elif data_sent == 'Ford':
        price = 11500
    elif data_sent == 'Ferrari':
        price = 160000
    elif data_sent == 'Lamborghini':
        price = 150000
    else:
        price = 26500
    return Response(price, mimetype='text/plain')