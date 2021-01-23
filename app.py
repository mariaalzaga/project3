from flask import Flask, render_template,request,jsonify
import os
from sqlalchemy.dialects import postgresql
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
#import psycopg2
import plotly.express as px

app = Flask(__name__)



@app.route("/")
def index():
    title = "Airline Stats and Visualizations"
    return render_template("index.html", title=title)

@app.route("/corelation")
def corelation():
    return render_template("corelation.html")

@app.route("/visuals")
def visuals():
    return render_template("visuals.html")

@app.route("/content")
def content():
    return render_template("content.html")

@app.route("/genre")
def genre():
    return render_template("genre.html")

@app.route("/heatmap")
def heatmap():
    return render_template("heatmap.html")

@app.route("/search")
def search():
    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)