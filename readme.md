## Online Bookstore API: Made with Python, Flask and Heroku

## How to run the app
Available on Postman for now.

## What users can do
- A user can create a store.
- A user can post items within a store.
- A user can change the item or pricing of the item.
- A user can delete the store or an item.
- A user can generate a list of all items or all stores.

## Features
1. Register as a user with username and password.
2. Authenticate user.
3. Post a new store.
4. Post a new item specifying store_id.
5. Get (generate) a list of all stores and corresponding items that belong to each store.
6. Get (generate) a list of all inventory.
7. Delete a store.
8. Delete items.
9. Put (change) items or their prices.

## Dependencies and Installation
Used virtualenv. To create virtualenv:
`pip3 install virtualenv`

`virtualenv venv `

`source venv/bin/activate`

Then install packages in the virtual environment. pip3 install the ff:
- Flask
- Flask-RESTFul
- Flask-JWT
- Flask-SQLAlchemy

## Here's a demo of the app running on [Postman](https://www.loom.com/share/27425c54cb8741d6aae0403fa05863ce)

Credits to [Teclado](https://github.com/tecladocode)
