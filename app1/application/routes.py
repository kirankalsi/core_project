from flask import Flask, render_template, redirect, url_for, request
import requests
import json

from application import app

@app.route('/', methods=['GET'])
def index():
    manufacturer = requests.get("http://34.89.59.226:5001/manufacturer")
    vehicle_type = requests.get("http://34.89.59.226:5002/vehicle_type")
    total_price = requests.post("http://34.89.59.226:5003/total_price", json={'manufacturer': manufacturer, 'vehicle_type': vehicle_type}.json()['total_price'])
    return render_template('index.html', manufacturer=manufacturer.text, vehicle_type=vehicle_type.text, total_price=total_price.text)