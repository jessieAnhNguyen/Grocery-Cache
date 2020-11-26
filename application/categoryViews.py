from application import app, db
from .forms import IndividualItemForm, IndividualCategoryForm
from flask import Flask, render_template, request, redirect, url_for, flash
from .database import db, Category, Main_List


# Add and update a category
@app.route("/category", methods=["GET", "POST"])
def viewAddCategory():
    mainForm = IndividualItemForm()
    categoryForm = IndividualCategoryForm()
    if request.method == "POST":
        if categoryForm.is_submitted() and categoryForm.validate():
            category_name = request.form["category_name"]
            description = request.form["description"]
            new_category = Category(
                category_name=category_name,
                description=description,
            )

            # Push to Database
            try:
                db.session.add(new_category)
                db.session.commit()
                return redirect(url_for("viewAddCategory"))
            except:
                return "Error"
        else:
            itemList = Main_List.query
            categoryList = Category.query
            # Will have to change to categories.html later
            return render_template("category.html", form=mainForm, cform=categoryForm, itemList=itemList, categoryList=categoryList)

    else:
        itemList = Main_List.query
        categoryList = Category.query
        # Will have to change to categories.html later
        return render_template("category.html", form=mainForm, cform=categoryForm, itemList=itemList, categoryList=categoryList)


# Update a category

@app.route("/category/update/<int:id>", methods=["GET", "POST"])
def updateCategory(id):
    # get the item from the database
    category_to_update = Category.query.get_or_404(id)
    categoryForm = IndividualCategoryForm()
    print(request.method)
    if request.method == "POST":
        if categoryForm.is_submitted() and categoryForm.validate():
            # get the updated values
            category_to_update.category_name = request.form["category_name"]
            category_to_update.description = request.form["description"]
            try:
                # update to the database
                db.session.commit()
                return redirect(url_for("viewAddCategory"))
            except:
                return "There was a problem updating the category item"
        else:
            return render_template("updateCategory.html", form=categoryForm, category_to_update=category_to_update)

    else:
        return render_template("updateCategory.html", form=categoryForm, category_to_update=category_to_update)

# TODO: message flash displayed to delete a category


@app.route("/category/delete/<int:id>", methods=["GET"])
def deleteCategory(id):
    category_to_delete = Category.query.get_or_404(id)
    try:
        db.session.delete(category_to_delete)
        db.session.commit()
        flash("You successfully deleted the category", "success")
        return redirect(url_for("viewAddCategory"))
    except:
        flash("There was an error deleting the category", "error")
        return "There was a problem deleting the category"
