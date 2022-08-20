import pymongo
from flask import Flask
from app import routes
from http import client

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["jetbov"]

def create_app():
    app = Flask(__name__, static_folder=None)

    routes.init_app(app)

    return app