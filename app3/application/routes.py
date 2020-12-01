from flask import Flask, Response, request
import random

from application import app

@app.route('/vehicle_type', methods=['GET'])
def vehicle_type():
    vehicle_types = ['Hatchback', 'Roadster', 'Pickup Truck', 'Sports Car', 'Saloon', 'Convertible', 'Hybrid']
    vehicle_type = random.choice(vehicle_types)
    return Response(vehicle_type, mimetype='text/plain')