from flask import Flask, Response, request
import random

from application import app

@app.route('/total_price', methods=['POST'])
def total_price():
    data_sent_app2 = request.data.decode('utf-8')
    if data_sent_app2 == 'Audi':
        man_price = 44500
    elif data_sent_app2 == 'BMW':
        man_price = 45000
    elif data_sent_app2 == 'Porsche':
        man_price = 99000
    elif data_sent_app2 == 'Ford':
        man_price = 11500
    elif data_sent_app2 == 'Ferrari':
        man_price = 160000
    elif data_sent_app2 == 'Lamborghini':
        man_price = 150000
    else:
        man_price = 26500

    data_sent_app3 = request.data.decode('utf-8')
    if data_sent_app3 == 'Hatchback':
        veh_price = 999
    elif data_sent_app3 == 'Roadster':
        veh_price = 12050
    elif data_sent_app3 == 'Pickup Truck':
        veh_price = 8888
    elif data_sent_app3 == 'Sports Car':
        veh_price = 20000
    elif data_sent_app3 == 'Saloon':
        veh_price = 3333
    elif data_sent_app3 == 'Convertible':
        veh_price = 21500
    else:
        veh_price = 9999

    total_price = man_price + veh_price
    return Response(total_price, mimetype='text/plain')