from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
# application = app

bootstrap = Bootstrap(app)
moment = Moment(app)

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../grocerycache.db")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+path

# Initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


app.config["SECRET_KEY"] = "Where do we go from here"

from application import categoryViews
from application import itemsViews
from application import views
from application import authViews

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
