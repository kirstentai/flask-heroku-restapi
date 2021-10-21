from flask import Flask
from flask_restful import Api, reqparse
from flask_jwt import JWT 

from security import authentiate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
#specify config property
# when an object has changed but not save to db, the extensions flask sqlalchemy keeps track of every change made to sqlalchemy session,
# but now we turn off cos sqlalchemy itself has a tracker that is better
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.secret_key = 'koalas1234'
api = Api(app)

# use flask decorator
@app.before_first_request
def create_tables():
    db.create_all()



jwt = JWT(app, authentiate, identity) #/auth, sends username, pw to authenticate func
    
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')

api.add_resource(UserRegister, '/register')


# dont run app (i.e. during import) unless app.py is ran
if __name__ == '__main__':
    from db import db #circular imports
    db.init_app(app)
    app.run(port=5000, debug=True)


