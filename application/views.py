from application import app, db
from .forms import IndividualItemForm, IndividualCategoryForm
from flask import Flask, render_template, request, redirect, url_for, flash
from .database import Main_List, Category

from flask_login import login_user, current_user, logout_user, login_required


# Add and view item on app.Main_List


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    mainForm = IndividualItemForm()
    categoryForm = IndividualCategoryForm()
    
    itemList = Main_List.query.filter_by(author=current_user)
    categoryList = Category.query.filter_by(author=current_user)
    return render_template("index.html", form=mainForm, cform=categoryForm, itemList=itemList, categoryList=categoryList)
