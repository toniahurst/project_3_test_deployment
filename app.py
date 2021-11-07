from pathlib import Path
import os
import sys
from bokeh.embed import components
from flask import Flask, render_template, url_for, request
import bokeh
import pandas as pd
## from util import make_plot
import csv
import json
import hvplot.pandas

app = Flask(__name__)

@app.route("/")
@app.route("/layout")
def index():
    return render_template("layout.html")

if __name__ == "__main__":
    
    app.run(debug = True)
    