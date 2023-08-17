from flask import redirect, request
from app import db
from models.product import Product

def add_product():
    if request.method == 'POST':
        product = Product(product_id = request.form['product_id'],product_name = request.form['Product_Name'])
        db.session.add(product)
        db.session.commit()
        return redirect('/')
    
def update_product(product_id):
    if request.method == 'POST':
        product = Product.query.filter_by(product_id=product_id).first()
        product.product_name = request.form['Product_Name']
        db.session.add(product)
        db.session.commit()
        return redirect('/')
    product = Product.query.filter_by(product_id=product_id).first()
    return product

def view_product(product_id):
    product = Product.query.filter_by(product_id=product_id).first()
    return product

