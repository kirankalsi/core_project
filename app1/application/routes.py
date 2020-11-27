from flask import Flask, render_template, redirect, url_for, request
import requests

from application import app

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')