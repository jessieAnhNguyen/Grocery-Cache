from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_moment import Moment
import os

app = Flask(__name__)
# application = app


bootstrap = Bootstrap(app)
moment = Moment(app)

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../grocerycache.db")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+path


app.config["SECRET_KEY"] = "Where do we go from here"
from application import views


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
