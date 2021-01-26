from flask import Flask, jsonify, render_template
import csv
import pandas as pd
import os
import json
import plotly
import plotly.graph_objects as go
import plotly.express as px

app = Flask(__name__)

def netflix_data():
    data = pd.read_csv("assets/data/ratings.csv")
    return data

def create_bargraph_plot():
    ratings = netflix_data()
    fig = px.bar(ratings, x = 'ratings', y='total',
             hover_data=['total'], color='total',
              height=400)
            

    fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
    fig.update_layout(title_text="Netflix Content Ratings")

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


@app.route("/")
def home():
    fig = create_bargraph_plot()
    return render_template("index.html", fig=fig)

if __name__ == "__main__":
    app.run(debug=True,port=5000)