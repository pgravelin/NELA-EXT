""" Import dependencies:
    - Flask framework API 
    - SQLAlchemy DB helper functions
    - psycopg2 PostgreSQL DB adapter """
    
from flask import Flask, render_template, json, jsonify, request, redirect, url_for
from flask_bootstrap import Bootstrap
from sqlalchemy.orm import load_only
from sqlalchemy import and_, or_
from database import db_session, POSTGRES, SQLALCHEMY_DATABASE_URI, cursor
from models.models import Articles
from forms.forms import FieldSelection, FieldSliders, text_fields
from datetime import date
import psycopg2 as dbapi

# Initialize Flask
app = Flask(__name__)

# Config
app.config["SECRET_KEY"] = b"\xce\x8e\xc7\x8b\\\x1c\x07\xfa\xda\xe3\xa2\xcd\x05"
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

Bootstrap(app)

@app.route("/")
def index():
    form = FieldSelection()
    return render_template("index.html", form=form)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/range_filter", methods=["POST"])
def range_filter():
    data = list(request.form)
    today = date.today().strftime('%m/%d/%y')
    form = FieldSliders(data[1:])
    
    return render_template("range_filter.html", form=form, today=today)

@app.route("/data", methods=["POST"])
def data():
    data = [(k, v) for k, v in request.form.items()] 
    fields, ranges = zip(*(data[:-1]))
    from_date, to_date = data[-1][1].split(" - ")

    converted_ranges = []
    for r in ranges:
        converted_ranges.append(list(map(int, "-100;100".split(";"))))
    
    # Query the POSTGRES database using dynamic SQL    
    cursor.execute("select * from Articles")
    
    q = "SELECT "
    for field in fields:
        q += "%s, " % field
        
    q = q.strip().strip(",")
    q += " FROM articles WHERE "
    
    for i in range(len(fields)):
        if not fields[i] in text_fields:
            q += "%s >= %f and %s <= %f" % (fields[i], converted_ranges[i][0], \
                    fields[i], converted_ranges[i][1])
        q += "and "
        
    q = q.strip().strip("and ")
    print(q)
    print(to_date)
    print(from_date)
    
    # print(cursor.fetchall())
    
    return render_template("data.html")

if __name__ == "__main__":
    app.run(debug=True)
    print("Working...")