from app import app
from models.product_movement import ProductMovement
from flask import render_template
from services.report_service import reportservice

@app.route('/report')
def report():
    report = reportservice.report()

    return render_template('report.html', report=report)