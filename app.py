"""from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<p>Hello, NEW World!</p>"

if __name__ == "__main__":
    
    app.run(debug = True)
"""


# Another example chaining Bokeh's to Flask.
from pathlib import Path
import os
import sys
from bokeh.embed import components
from flask import Flask, render_template, url_for, request
import bokeh
import pandas as pd
from util import make_plot
import csv
import json
import hvplot.pandas
"""
Read in the JSON files
"""
df = pd.read_json('F_T_W copy/ada_fund.json')

length = len(df)
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/df")
def dataframe():
    return render_template("df.html", length=length, dataframe=df.to_html())


@app.route("/dfcustom")
def dfcustom():
    data = df.to_dict(orient="records")
    headers = df.columns
    print(headers)
    return render_template("dfcustom.html", data=data, headers=headers)

@app.route("/rocrybot")
def rocrybot():
    return render_template("rocrybot.html")

@app.route("/visualizations")
def visualizations():
    return render_template("visualizations.html", name="Visualizations")

@app.route("/tables")
def tables():
    return render_template("tables.html", name="Tables")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html", name="About Us")

@app.route("/articles")
def articles():
    return render_template("articles.html", name="Articles")

@app.route("/portfolios")
def portfolios():
    return render_template("portfolios.html", name="Portfolios")

@app.route("/moreinfo")
def more_info():
    return render_template("moreinfo.html")

@app.route("/home")
def home():
    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True, port=5957)