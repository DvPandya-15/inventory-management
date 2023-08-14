from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db';
db = SQLAlchemy(app)

class Product(db.Model):
    product_id = db.Column(db.String(50), primary_key=True)
    product_name = db.Column(db.String(50))
    product_qty = db.Column(db.Integer)
    product_location = db.Column(db.String(50))

    def __repr__(self):
        return f"{self.product_name}"
    
class Location(db.Model):
    location_id = db.Column(db.String(50), primary_key=True)
    location_name = db.Column(db.String(50), db.ForeignKey('product.product_location'))


class ProductMovement(db.Model):
    movement_id = db.Column(db.String(50), primary_key=True)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)
    from_location = db.Column(db.String(50), db.ForeignKey('location.location_name'))
    to_location = db.Column(db.String(50), db.ForeignKey('location.location_name'))
    product_name = db.Column(db.String(50), db.ForeignKey('product.product_name'))
    qty = db.Column(db.Integer, nullable=False)    

@app.route('/', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product = Product(product_id = request.form['product_id'],product_name = request.form['Product_Name'])
        db.session.add(product)
        db.session.commit()
        return redirect('/')
    allProducts = Product.query.all()
    locations = Location.query.all()
    query = '''
        SELECT pm.product_name as name, SUM(pm.qty) AS total_quantity
        FROM product_movement pm,product p
        WHERE pm.product_name = p.product_name
        '''

    with db.engine.connect() as conn:
        result = conn.execute(text(query))
        conn.commit()
    
    product_qty_list = result


    return render_template('index.html', allProducts=allProducts,product_qty_list =product_qty_list)

@app.route('/update/<int:product_id>',methods=['GET','POST'])
def update_product(product_id):
    if request.method == 'POST':
        product = Product.query.filter_by(product_id=product_id).first()
        product.product_name = request.form['Product_Name']
        # product.product_qty = request.form['product_qty']
        # product.product_location = request.form['product_location']

        db.session.add(product)
        db.session.commit()
        return redirect('/')
    
    product = Product.query.filter_by(product_id=product_id).first()
    return render_template('update.html', product=product)


@app.route('/view/<int:product_id>',methods=['GET','POST'])
def view_product(product_id):
    product = Product.query.filter_by(product_id=product_id).first()
    return render_template('view_product.html', product=product)

@app.route('/delete/<int:product_id>',methods=['GET']) 
def delete(product_id):
    product = Product.query.filter_by(product_id = product_id).first()
    db.session.delete(product)
    db.session.commit()
    return redirect("/")

@app.route('/add/location',methods=['GET','POST'])
def add_location():
    if request.method == 'POST':
        location = Location(location_id = request.form['location_id'],location_name = request.form['location_name'])
        db.session.add(location)
        db.session.commit()
    allLocation = Location.query.all()
    return render_template('location.html', allLocation=allLocation)


@app.route('/add/product_movement', methods=['GET', 'POST'])
def add_product_movement():
    products = Product.query.all()
    locations = Location.query.all()

    if request.method == 'POST':
        movement_id = request.form['movement_id']
        product_name = request.form['product_name']
        from_location = request.form['from_location'] or None
        to_location = request.form['to_location'] or None
        qty = int(request.form['qty'])

        new_movement = ProductMovement(movement_id = movement_id, product_name=product_name, from_location=from_location,
                                       to_location=to_location, qty=qty)
        db.session.add(new_movement)
        db.session.commit()

    productMovements = ProductMovement.query.all()
    return render_template('product_movement_form.html', movement=None,
                           products=products, locations=locations, productMovements = productMovements)


@app.route('/report')
def report():
    report = ProductMovement.query.all()

    return render_template('report.html', report=report)


if __name__ == "__main__":
    app.run(debug=True)
