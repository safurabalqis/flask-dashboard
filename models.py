from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sales(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(50))
    amount = db.Column(db.Integer)
