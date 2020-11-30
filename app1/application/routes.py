from flask import Flask, render_template, redirect, url_for, request
import requests

from application import app

@app.route('/', methods=['GET'])
def index():
    manufacturer = requests.get("http://34.105.145.24:5001/manufacturer")
    vehicle_type = requests.get("http://34.105.145.24:5002/vehicle_type")
    total_price = requests.post("http://34.105.145.24:5003/total_price", data=manufacturer.text)
    return render_template('index.html', manufacturer=manufacturer.text, vehicle_type=vehicle_type.text, data2=manufacturer.text, data3=vehicle_type.text)