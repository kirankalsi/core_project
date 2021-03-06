from flask import Flask, Response, request
import random

from application import app

@app.route('/total_price', methods=['GET', 'POST'])
def total_price():
    data = request.get_json()
    man = data['manufacturer']
    veh = data['vehicle_type']

    if man == 'AUDI':
        man_price = 44500
    elif man == 'BMW':
        man_price = 45000
    elif man == 'PORSCHE':
        man_price = 99000
    elif man == 'FORD':
        man_price = 11500
    elif man == 'FERRARI':
        man_price = 160000
    elif man == 'LAMBORGHINI':
        man_price = 150000
    else:
        man_price = 26500

    if veh == 'HHHatchback':
        veh_price = 999
    elif veh == 'RRRoadster':
        veh_price = 12050
    elif veh == 'PPPickup Truck':
        veh_price = 8888
    elif veh == 'SSSports Car':
        veh_price = 20000
    elif veh == 'SSSaloon':
        veh_price = 3333
    elif veh == 'CCConvertible':
        veh_price = 21500
    else:
        veh_price = 9999
    
    total_price = (man_price + veh_price)*20
    return str(total_price)