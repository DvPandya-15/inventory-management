from app import db

class Location(db.Model):
    location_id = db.Column(db.String(50), primary_key=True)
    location_name = db.Column(db.String(50), db.ForeignKey('product.product_location'))