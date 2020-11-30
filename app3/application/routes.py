from flask import Flask, Response, request
import random

from application import app

@app.route('/vehicle_type', methods=['GET'])
def vehicle_type():
    vehicle_type = ['Hatchback', 'Roadster', 'Pickup Truck', 'Sports Car', 'Saloon', 'Convertible', 'Hybrid']
    vehicle_type = random.choice(vehicle_type)
    return Response(vehicle_type, mimetype='text/plain')

@app.route('/veh_price', methods=['POST'])
def veh_price():
    data_sent = request.data.decode('utf-8')
    if data_sent == 'Hatchback':
        veh_price = 999
    elif data_sent == 'Roadster':
        veh_price = 12050
    elif data_sent == 'Pickup Truck':
        veh_price = 8888
    elif data_sent == 'Sports Car':
        veh_price = 20000
    elif data_sent == 'Saloon':
        veh_price = 3333
    elif data_sent == 'Convertible':
        veh_price = 21500
    else:
        veh_price = 9999
    return Response(veh_price, mimetype='text/plain')