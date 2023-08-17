from models.location import Location
from flask import request
from app import db

def get_locations():
    if request.method == 'POST':
        location = Location(location_id = request.form['location_id'],location_name = request.form['location_name'])
        db.session.add(location)
        db.session.commit()
    all_locations = Location.query.all()
    return all_locations