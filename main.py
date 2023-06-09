from flask import Flask,render_template,request
from flask_sqlaclhemy import SQLAlchemy
import psycopg2
import psycopg2.extras

app=Flask(__name__)
db=SQLALCHEMY(app)
app.config=

@app.route("/")
def home():
    return render_template("Home_dashboard.html")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit",method=['post'])
def submit():
    return render_template("Home_dashboard")


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/")
def login():
    return render_template("login.html")
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')