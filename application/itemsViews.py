from application import app, db
from .forms import IndividualItemForm, IndividualCategoryForm
from flask import Flask, render_template, request, redirect, url_for, flash
from .database import Main_List, Category

from flask_login import login_user, current_user, logout_user, login_required


# Add and update an item to app.Main_List


@app.route("/items", methods=["GET", "POST"])
@login_required
def viewAddItems():
    mainForm = IndividualItemForm()
    categoryForm = IndividualCategoryForm()
    if request.method == "POST":
        if mainForm.is_submitted() and mainForm.validate():
            item_name = request.form["item_name"]
            category = request.form["category"]
            quantity = request.form["quantity"]
            budget = request.form["budget"]
            urgency_level = request.form["urgency_level"]
            notes = request.form["notes"]
            author = current_user

            new_item = Main_List(
                item_name=item_name,
                quantity=quantity,
                budget=budget,
                urgency_level=urgency_level,
                notes=notes,
                author = author
            )

            # Push to Database
            try:
                db.session.add(new_item)
                db.session.commit()
                return redirect(url_for("viewAddItems"))
            except:
                return "Error"
        else:
            itemList = Main_List.query.filter_by(author=current_user).all()
            categoryList = Category.query.all()
            return render_template("items.html", form=mainForm, cform=categoryForm, itemList=itemList, categoryList=categoryList)

    else:
        itemList = Main_List.query.filter_by(author=current_user).all()
        categoryList = Category.query.all()

        next_page = request.args.get('next')
        
        print('Helo')
        print(next_page)
        if next_page == 'items':
            return render_template("items.html", form=mainForm, cform=categoryForm, itemList=itemList, categoryList=categoryList)
        elif next_page == 'index':
            return render_template("index.html", form=mainForm, cform=categoryForm, itemList=itemList, categoryList=categoryList)
        return render_template("items.html", form=mainForm, cform=categoryForm, itemList=itemList, categoryList=categoryList)


# Update an item in app.Main_List

@app.route("/items/update/<int:id>", methods=["GET", "POST"])
@login_required
def update(id):
    # get the item from the database
    item_to_update = Main_List.query.get_or_404(id)
    mainForm = IndividualItemForm()
    if request.method == "POST":
        if mainForm.is_submitted() and mainForm.validate():
            # get the updated values
            item_to_update.item_name = request.form["item_name"]
            item_to_update.quantity = request.form["quantity"]
            item_to_update.budget = request.form["budget"]
            item_to_update.urgency_level = request.form["urgency_level"]
            item_to_update.notes = request.form["notes"]
            try:
                # update to the database
                db.session.commit()
                return redirect(url_for("index"))
            except:
                return "There was a problem updating the grocery item"
        else:
            return render_template("updateItem.html", form=mainForm, item_to_update=item_to_update)

    else:
        return render_template("updateItem.html", form=mainForm, item_to_update=item_to_update)

# TODO: message flash displayed to delete an item in app.Main_List


@app.route("/items/delete/<int:id>", methods=["GET"])
@login_required
def delete(id):
    item_to_delete = Main_List.query.get_or_404(id)
    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        flash("You successfully deleted the grocery item", "success")
        return redirect(url_for("index"))
    except:
        flash("There was an error deleting the grocery item", "error")
        return "There was a problem updating the grocery item"

