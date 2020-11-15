from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap


app = Flask(__name__)
application = app

bootstrap = Bootstrap(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


@app.route("/")
def index():
    return "<h1>Test World!</h1>"
