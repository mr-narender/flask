from flask import Flask
from flask_pymongo import PyMongo

from .config import MONGO_URI

# initialize the Flask app
app = Flask(__name__)

# connect and create a db named as mydb
app.config["MONGO_URI"] = MONGO_URI

# initializing the client for mongodb
mongo = PyMongo(app)

# register blueprints
from .views import admin
from .views import home

app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(home, url_prefix="/")
