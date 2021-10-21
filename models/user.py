import sqlite3 
from db import db

#not a resource, but a helper. model is an internal representation of an entity
# is an API with 2 endpoints (classmethod)
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # column called id, primary key
    username = db.Column(db.String(80)) # limit 80 chars
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        # no need to specify id since auto generated upon creating user
        # self.id = _id 
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id): #find by id
        return cls.query.filter_by(id=_id).first()
