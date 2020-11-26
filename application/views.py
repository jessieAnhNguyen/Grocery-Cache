from application import app, db
from .forms import IndividualItemForm, IndividualCategoryForm
from flask import Flask, render_template, request, redirect, url_for, flash
from .database import Main_List, Category

# Add and update an item to app.Main_List


@app.route("/", methods=["GET", "POST"])
def index():
    mainForm = IndividualItemForm()
    categoryForm = IndividualCategoryForm()
    
    itemList = Main_List.query
    categoryList = Category.query
    return render_template("index.html", form=mainForm, cform=categoryForm, itemList=itemList, categoryList=categoryList)
