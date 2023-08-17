from models.product import Product
from models.location import Location
from models.product_movement import ProductMovement
from flask import render_template, request
from app import db,app
from services.productmovement_service import productmoevementservice

@app.route('/product-movement', methods=['GET', 'POST'])
def get_product_movement():
    products = productmoevementservice.get_all_products()
    locations = productmoevementservice.get_all_locations()
    productmoveements = productmoevementservice.get_product_movements()
    return render_template('product_movement_form.html', movement=None,
                           products=products, locations=locations, productMovements = productmoveements)

