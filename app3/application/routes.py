from flask import Flask, Response, request
import random

from application import app

@app.route('/vehicle_type', methods=['GET'])
def vehicle_type():
    vehicle_types = ['HHHatchback', 'RRRoadster', 'PPPickup Truck', 'SSSports Car', 'SSSaloon', 'CCConvertible', 'HHHybrid']
    vehicle_type = random.choice(vehicle_types)
    return Response(vehicle_type, mimetype='text/plain')