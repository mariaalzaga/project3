from flask import Flask, jsonify, render_template, request, make_response
import requests
import pandas as pd
import os
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")