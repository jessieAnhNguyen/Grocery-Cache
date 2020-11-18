from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from forms import IndividualItemForm


app = Flask(__name__)
application = app

bootstrap = Bootstrap(app)
moment = Moment(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///grocerycache.db"
# Initialize the database
db = SQLAlchemy(app)


# Create db model
class Main_List(db.Model):
    item_ID = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(), nullable=False)
    category = db.Column(db.String(), nullable=True)
    budget = db.Column(db.Float, nullable=True)
    urgency_level = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(), nullable=True)

    # Create a funcion to return a string when we add something
    def __repr__(self):
        return "<Name %r>" % self.item_ID


app.config["SECRET_KEY"] = "Where do we go from here"


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

# Update an item


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    # get the item from the database
    item_to_update = Main_List.query.get_or_404(id)
    mainForm = IndividualItemForm()
    if request.method == "POST":
        if mainForm.is_submitted() and mainForm.validate():
            # get the updated values
            item_to_update.item_name = request.form["item_name"]
            item_to_update.category = request.form["category"]
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
            return render_template("update.html", form=mainForm, item_to_update=item_to_update)

    else:
        return render_template("update.html", form=mainForm, item_to_update=item_to_update)

# TODO: write the delete an item function


@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    item_to_delete = Main_List.query.get_or_404(id)
    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        flash("You successfully deleted the ingredient", "success")
        return redirect(url_for("index"))
    except:
        flash("There was an error deleting the ingredient", "error")
        return "There was a problem updating the recipe"

# Read the main list


@app.route("/", methods=["GET", "POST"])
def index():
    mainForm = IndividualItemForm()

    if request.method == "POST":
        if mainForm.is_submitted() and mainForm.validate():
            item_name = request.form["item_name"]
            category = request.form["category"]
            budget = request.form["budget"]
            urgency_level = request.form["urgency_level"]
            notes = request.form["notes"]

            new_item = Main_List(
                item_name=item_name,
                category=category,
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
            return render_template("index.html", form=mainForm, itemList=itemList)

    else:
        itemList = Main_List.query
        return render_template("index.html", form=mainForm, itemList=itemList)
