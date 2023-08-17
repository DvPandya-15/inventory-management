from app import db

class Product(db.Model):
    product_id = db.Column(db.String(50), primary_key=True)
    product_name = db.Column(db.String(50))
    product_qty = db.Column(db.Integer)
    product_location = db.Column(db.String(50))

    def __repr__(self):
        return f"{self.product_name}"