from models.product import Product
from flask import render_template, redirect, request
from app import db,app
from services.product_service import productservice

@app.route('/products', methods=['GET', 'POST'])
def add_product():
    productservice.add_product()
    return render_template('index.html')

@app.route('/products/<int:product_id>',methods=['GET','POST'])
def update_product(product_id):
    product = productservice.update_product(product_id)
    return render_template('update.html', product=product)

@app.route('/products/<int:product_id>',methods=['GET','POST'])
def view_product(product_id):
    product = productservice.view_product(product_id)
    return render_template('view_product.html', product=product)

@app.route('/products/<int:product_id>',methods=['GET']) 
def delete(product_id):
    productservice.delete_product(product_id)