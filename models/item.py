import sqlite3
from typing import ItemsView
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
    
    def json(self):
        return {'name': self.name, 'price': self.price}


    @classmethod #remains classmethod because it returns ItemModel object
    def find_by_name(cls, name):
      
        return cls.query.filter_by(name=name).first() # returns ItemModel object: SELECT * FROM items WHERE name=name LIMIT 1;



    def save_to_db(self): # instead of inserting data, it's now updating data
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()