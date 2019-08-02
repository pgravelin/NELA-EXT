from flask import Flask, render_template, json, jsonify, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
from database import db_session, POSTGRES, SQLALCHEMY_DATABASE_URI
from models.models import Articles
from forms.forms import FieldSelection, FieldSliders
import psycopg2 as dbapi
import sqlalchemy

# Initialize Flask
app = Flask(__name__)

app.config["SECRET_KEY"] = b"\xce\x8e\xc7\x8b\\\x1c\x07\xfa\xda\xe3\xa2\xcd\x05"
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

Bootstrap(app)

@app.route("/")
def homepage():
    form = FieldSelection()
    return render_template("home.html", form=form)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/range_filter", methods=["POST"])
def range_filter():
    data = request.form
    print(data)
    form = FieldSliders(list(data)[1:])
    return render_template("range_filter.html", form=form)

@app.route("/data", methods=["POST"])
def data():
    data = request.form
    print(data)
    return render_template("data.html")

if __name__ == "__main__":
    app.run(debug=True)
    print("Working...")