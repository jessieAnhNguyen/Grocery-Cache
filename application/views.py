from application import app, db
from .forms import IndividualItemForm, IndividualCategoryForm
from flask import Flask, render_template, request, redirect, url_for, flash
from .database import Itemtable, Category

from flask_login import login_user, current_user, logout_user, login_required


# Add and view item on app.Itemtable


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    mainForm = IndividualItemForm()
    categoryForm = IndividualCategoryForm()
    
    itemList = Itemtable.query.filter_by(author=current_user).all()
    categoryList = Category.query.filter_by(author=current_user).all()
    return render_template("index.html", form=mainForm, cform=categoryForm, itemList=itemList, categoryList=categoryList)
