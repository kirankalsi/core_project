from flask import Flask, render_template, redirect, url_for, request
import requests
from application.models import Vehicles
from application import app, db

@app.route('/', methods=['GET', 'POST'])
def index():
    manufacturer = requests.get("http://34.105.145.24:5001/manufacturer")
    vehicle_type = requests.get("http://34.105.145.24:5002/vehicle_type")
    dictionary = {'manufacturer': manufacturer.text, 'vehicle_type': vehicle_type.text}
    total_price = requests.post("http://34.105.145.24:5003/total_price", json=dictionary)

    db_info = Vehicles(manufacturer=manufacturer.text, vehicle_type=vehicle_type.text, total_price=total_price.text)
    db.session.add(db_info)
    db.session.commit()

    return render_template('index.html', manufacturer=manufacturer.text, vehicle_type=vehicle_type.text, total_price=total_price.text)