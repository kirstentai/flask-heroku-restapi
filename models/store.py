from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    #backref
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name
    
    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}


    @classmethod #remains classmethod because it returns ItemModel object
    def find_by_name(cls, name):
      
        return cls.query.filter_by(name=name).first() # returns ItemModel object: SELECT * FROM items WHERE name=name LIMIT 1;



    def save_to_db(self): # instead of inserting data, it's now updating data
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()