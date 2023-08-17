from app import db
from datetime import datetime

class ProductMovement(db.Model):
    movement_id = db.Column(db.String(50), primary_key=True)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)
    from_location = db.Column(db.String(50), db.ForeignKey('location.location_name'))
    to_location = db.Column(db.String(50), db.ForeignKey('location.location_name'))
    product_name = db.Column(db.String(50), db.ForeignKey('product.product_name'))
    qty = db.Column(db.Integer, nullable=False)  