from datetime import datetime
from pytz import timezone
from hello_city import app
from flask import render_template


@app.route('/')
def home():
    return render_template("pages/home.html", date=datetime.now(timezone('America/Toronto')))


@app.route('/about-us/')
def about():
	return render_template("pages/about.html", date=datetime.now(timezone('America/Toronto')))