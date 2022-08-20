from concurrent.futures import process
import pymongo
from flask import Flask
from app import routes
from http import client
from os import getenv

DATABASE_NAME = getenv("DB_NAME")

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client[DATABASE_NAME]

def create_app():
    app = Flask(__name__, static_folder=None)
    
    routes.init_app(app)

    return app