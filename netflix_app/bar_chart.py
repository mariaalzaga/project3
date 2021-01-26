from flask import Flask, jsonify, render_template
import csv
import pandas as pd
import os
import json
import plotly
import plotly.graph_objects as go
import plotly.express as px

app = Flask(__name__)

def revenue_data():
    revenue = pd.read_csv("assets/raw_data/revenue_growth_final.csv")
    return revenue

def create_bargraph_plot():
    data = revenue_data()
    fig1 = px.bar(data,
             x='date',
             y='revenue',
             title='Revenue by Region Q1 2018 - Q2 2020',
             color='area',
             barmode='group')

    fig1.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
    fig1.update_layout(title_text="Netflix Revenue by Area (2018 - 2020)")

    return json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

@app.route("/")
def home():
    fig1 = create_bargraph_plot()
    return render_template("index.html", fig1=fig1)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
