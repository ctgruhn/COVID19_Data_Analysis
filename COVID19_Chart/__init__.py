from flask import Flask
import csv, json, os.path
import datetime
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc'

from COVID19_Chart import routes