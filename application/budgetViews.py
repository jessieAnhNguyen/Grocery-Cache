from application import app, db
from flask import Flask, render_template, request, redirect, url_for, flash
from .forms import IndividualItemForm, IndividualCategoryForm
from flask_login import login_user, current_user, logout_user, login_required
from .database import Itemtable, Category
from sqlalchemy.sql import func


@app.route("/budget", methods=["GET", "POST"])
@login_required
def viewBudget():
    mainForm = IndividualItemForm()
    categoryForm = IndividualCategoryForm()
    itemList = Itemtable.query.filter_by(author=current_user).all()
    sum = 0
    for items in itemList:
        #print (items.user_id)
        sum += items.budget
    print(sum)

    #sum_budget = db.session.query(func.sum(Itemtable.budget).label('sum')).filter_by(Itemtable.user_id==current_user)
    #print (sum_budget)
    return render_template("budget.html", form=mainForm, cform=categoryForm, itemList=itemList, total=sum)
