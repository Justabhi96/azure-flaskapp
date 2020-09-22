from flask import Flask
from datetime import date, timedelta

app = Flask(__name__)


@app.route("/")
def home():
    return "Simple flask API"


@app.route("/today")
def today():
    return {"today": date.today()}


@app.route("/tomorrow")
def tomorrow():
    return {"tomorrow": date.today() + timedelta(days=1)}
