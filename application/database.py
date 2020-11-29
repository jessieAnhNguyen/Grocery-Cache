from application import app, db, login_manager
from flask_login import UserMixin
# Create db model of an item


class Main_List(db.Model):
    item_ID = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(), nullable=False)
    quantity = db.Column(db.Float, nullable=True)
    budget = db.Column(db.Float, nullable=True)
    urgency_level = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(), nullable=True)

    # Create a funcion to return a string when we add something
    def __repr__(self):
        return "<Name %r>" % self.item_ID

# Create db model of Category


class Category(db.Model):
    category_ID = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=True)

    # Create a funcion to return a string when we add something
    def __repr__(self):
        return "<Name %r>" % self.category_ID

# Create db model of a user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    urgency_level = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(), nullable=True)

    # Create a funcion to return a string when we add something
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    # Create a funcion to return user id
    def get_id(self):
           return (self.user_id)