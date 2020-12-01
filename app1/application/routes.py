from flask import Flask, render_template, redirect, url_for, request
import requests

from application import app

@app.route('/', methods=['GET'])
def index():
    manufacturer = requests.get("http://35.246.108.117:5001/manufacturer")
    vehicle_type = requests.get("http://35.246.108.117:5002/vehicle_type")
    dictionary = {'manufacturer': manufacturer.text, 'vehicle_type': vehicle_type.text}
    total_price = requests.post("http://35.246.108.117:5003/total_price", json=dictionary)
    return render_template('index.html', manufacturer=manufacturer.text, vehicle_type=vehicle_type.text, total_price=total_price.text)