from models.product import Product
from models.location import Location
from models.product_movement import ProductMovement
from flask import request
from app import db

def get_all_products():
    products = Product.query.all()
    return products

def get_all_locations():
    locations = Location.query.all()
    return locations   


def get_product_movements():
    if request.method == 'POST':
        new_movement = ProductMovement(movement_id = request.form['movement_id'], product_name=request.form['product_name'], from_location=request.form['from_location'] or '',
                                       to_location=request.form['to_location'] or '', qty=int(request.form['qty']))
        db.session.add(new_movement)
        db.session.commit()

    productMovements = ProductMovement.query.all()
    return productMovements