from models.location import Location
from flask import render_template
from app import app
from services.location_service import locationservices


@app.route('/locations',methods=['GET','POST'])
def get_location():
    all_locations = locationservices.get_locations()
    return render_template('location.html', all_locations=all_locations)