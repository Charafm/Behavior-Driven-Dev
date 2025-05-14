# service/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80))
    available = db.Column(db.Boolean, default=True)
    price = db.Column(db.Float)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'available': self.available,
            'price': self.price
        }

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def find(cls, id):
        return cls.query.get(id)

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).all()

    @classmethod
    def find_by_category(cls, category):
        return cls.query.filter_by(category=category).all()

    @classmethod
    def find_by_availability(cls, available):
        return cls.query.filter_by(available=available).all()

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()