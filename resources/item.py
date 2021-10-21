# import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank."
    )

    parser.add_argument('store_id',
        type=float,
        required=True,
        help="Every item needs a store id."
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404
  
    def post(self, name): 
        #checking item is not already in database
        if ItemModel.find_by_name(name): # or Item.find_by_name(name)
            return {'message': "An item with name '{}' already exists.".format(name) }, 400 #something wrong with request

        # parse data
        data = Item.parser.parse_args()

        # create json item
        # item = {'name': name, 'price': data['price']}
        item = ItemModel(name, **data)  #unpacks data['price'], data['store_id']
        
        # deal with exception
        try:
            # ItemModel.insert(item)
            item.save_to_db()
        except:
            return {"message": "Error occurred inserting the item."}, 500 #500 nothing wrong w request, internal server error
        
        
        return item, 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}

    def put(self, name):      
        # data = request.get_json()
        data = Item.parser.parse_args()

        # find if item exists
        # item = next(filter(lambda x: x['name'] == name, items), None)
        item = ItemModel.find_by_name(name)

        if item is None: # if item is none, we save to db
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
        
        
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        # items = []

        # for row in result:
        #     items.append({'name': row[0], 'price': row[1]})

        # connection.commit()
        # connection.close()

        # return {'items': items}
        return {'items': [item.json() for item in ItemModel.query.all()]}

        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
