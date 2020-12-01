from flask import Flask, Response, request
import random

from application import app

@app.route('/manufacturer', methods=['GET'])
def manufacturer():
    manufacturers = ['Audi', 'BMW', 'Porsche', 'Ford', 'Ferrari', 'Lamborghini', 'Toyota']
    manufacturer = random.choice(manufacturers)
    return Response(manufacturer, mimetype='text/plain')

'''
@app.route('/man_price', methods=['POST'])
def man_price():
    data_sent = request.data.decode('utf-8')
    if data_sent == 'Audi':
        man_price = 44500
    elif data_sent == 'BMW':
        man_price = 45000
    elif data_sent == 'Porsche':
        man_price = 99000
    elif data_sent == 'Ford':
        man_price = 11500
    elif data_sent == 'Ferrari':
        man_price = 160000
    elif data_sent == 'Lamborghini':
        man_price = 150000
    else:
        man_price = 26500
    return Response(man_price, mimetype='text/plain')
'''