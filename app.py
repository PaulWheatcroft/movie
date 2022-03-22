# save this as app.py
from flask import (
                    Flask, escape, request, flash, render_template,
                    redirect, request, session, url_for)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "home.html")
