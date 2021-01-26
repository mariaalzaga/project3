from flask import Flask, jsonify, render_template
import csv
import pandas as pd
import os
import json
import plotly
import plotly.graph_objects as go
import plotly.express as px

app = Flask(__name__)

def subscriber_data():
    subscriber = pd.read_csv("assets/raw_data/DataNetflixSubscriber2020_V2.csv")
    return subscriber

def create_subscriber_plot():
    data2 = subscriber_data()
    fig2 = px.bar(data2,
             x='Years',
             y='Subscribers',
             title='Subscribers by Region Q1 2018 - Q2 2020',
             color='Area',
             barmode='group')

    fig2.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
    fig2.update_layout(title_text="Netflix Subscribers by Area (2018 - 2020)")

    return json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

@app.route("/")
def home():
    fig1 = create_bargraph_plot()
    return render_template("index.html", fig1=fig1)

@app.route("/subscribers")
def subscribers():
    fig2 = create_subscriber_plot()
    return render_template("subscribers.html", fig2=fig2)

if __name__ == "__main__":
    app.run(debug=True,port=5000)