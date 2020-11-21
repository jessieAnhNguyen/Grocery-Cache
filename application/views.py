from application import app, db
from .forms import IndividualItemForm
from flask import Flask, render_template, request, redirect, url_for, flash
from .database import Main_List

# Add and view item on app.Main_List


@app.route("/", methods=["GET", "POST"])
def index():
    mainForm = IndividualItemForm()

    if request.method == "POST":
        if mainForm.is_submitted() and mainForm.validate():
            item_name = request.form["item_name"]
            quantity = request.form["quantity"]
            budget = request.form["budget"]
            urgency_level = request.form["urgency_level"]
            notes = request.form["notes"]

            new_item = Main_List(
                item_name=item_name,
                quantity=quantity,
                budget=budget,
                urgency_level=urgency_level,
                notes=notes,
            )

            # Push to Database
            try:
                db.session.add(new_item)
                db.session.commit()
                return redirect(url_for("index"))
            except:
                return "Error"
        else:
            itemList = Main_List.query
            return render_template("mainList.html", form=mainForm, itemList=itemList)

    else:
        itemList = Main_List.query
        return render_template("mainList.html", form=mainForm, itemList=itemList)


# Update an item in app.Main_List

@app.route("/item/update/<int:id>", methods=["GET", "POST"])
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


@app.route("/item/delete/<int:id>", methods=["GET"])
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
