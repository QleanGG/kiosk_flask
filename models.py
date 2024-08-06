# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    company = db.Column(db.String(64), nullable=False)
    kosher = db.Column(db.Boolean, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    expiration_date = db.Column(db.Date, nullable=True)
    
    def __str__(self):
        return f"{self.title} - {self.company} - Kosher: {self.kosher} - amount: {self.amount} expires: {self.expiration_date}"


