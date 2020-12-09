from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    IntegerField,
    FloatField,
    BooleanField,
    SelectField
)

from application import  db


from wtforms.ext.sqlalchemy.fields import QuerySelectField,QuerySelectMultipleField

from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange, ValidationError
from .database import User,Category

from flask_login import login_user, current_user, logout_user, login_required


# Form to add/update an item in Itemtable
@login_required
def category_choices():      
    return db.session.query(Category).filter_by(author=current_user).all()

class IndividualItemForm(FlaskForm):
    item_name = StringField("Item Name", validators=[
        DataRequired(),
        Length(max=200, message="Item name must be less than 200 characters"),
    ])
    quantity = FloatField("Quantity", validators=[
        NumberRange(
            min=0, message="Quantity can't be negative"),
    ])
    
    category = QuerySelectMultipleField(u'Categories',
                                allow_blank=True,
                                query_factory=category_choices)

    budget = FloatField("Budget (in USD)", validators=[NumberRange(
        min=0, message="Budget can't be negative"), ])
    urgency_level = IntegerField("Urgency Level", validators=[NumberRange(
        min=1, max=5, message="Urgency level must be between 1-5"), ])
    notes = StringField("Other notes", validators=[
        Length(max=500, message="Notes must be less than 500 characters"),
    ])
    submit = SubmitField("Submit")

# Form to add/update a category


class IndividualCategoryForm(FlaskForm):
    category_name = StringField("Category Name", validators=[DataRequired(),
                                                             Length(
                                                                 max=200, message="Category must be less than 200 characters"),
                                                             ])
    description = StringField("Description of category", validators=[
        Length(max=1000, message="Description must be less than 1000 characters"),
    ])
    submit = SubmitField("Submit")


# Form to register an account


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(),
                                                             Length(min=1,
                                                                 max=200, message="Username must be less than 200 characters"),
                                                             ])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username already exists.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email already exists.')                                      

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_user = BooleanField('Remember Me')
    submit = SubmitField('Login')