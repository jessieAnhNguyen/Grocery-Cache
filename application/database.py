from application import app, db

# Create db model of an item
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

# Create db model of Category
class Category(db.Model):
    # __bind_key__ = 'categoryTable'
    category_ID = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=True)

    # Create a funcion to return a string when we add something
    def __repr__(self):
        return "<Name %r>" % self.category_ID