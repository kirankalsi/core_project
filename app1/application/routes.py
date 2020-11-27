from flask import Flask, render_template, redirect, url_for, request
import requests

from application import app

@app.route('/', methods=['GET'])
def index():
    manufacturer = requests.get("http://35.242.189.130:5001/manufacturer")
    return render_template('index.html', manufacturer=manufacturer.text)