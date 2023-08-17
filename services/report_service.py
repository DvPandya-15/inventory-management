from models.product_movement import ProductMovement

def report():
    report = ProductMovement.query.all()
    return report