from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
    SelectField,
    IntegerField,
    DateField,
    FloatField,
    RadioField,
)

from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange


class IndividualItemForm(FlaskForm):
    item_name = StringField("Item Name", validators=[
        DataRequired(),
        Length(max=200, message="Item name must be less than 200 characters"),
    ])
    category = StringField("Category", validators=[
        Length(max=200, message="Category must be less than 200 characters"),
    ])
    budget = FloatField("Budget (in USD)", validators=[NumberRange(
        min=0, message="Budget can't be negative"), ])
    urgency_level = IntegerField("Urgency Level", validators=[NumberRange(
        min=1, max=5, message="Urgency level must be between 1-5"), ])
    notes = StringField("Other notes", validators=[
        Length(max=500, message="Notes must be less than 500 characters"),
    ])
    submit = SubmitField("Submit")
