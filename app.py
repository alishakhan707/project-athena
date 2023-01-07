from flask import Flask, request
from pymongo import MongoClient
import json
import dotenv
import os

dotenv.load_dotenv()
app = Flask(__name__)
db = MongoClient(os.environ['MONGODB_CONNECTION_STRING'])['athena']

# homepage
@app.get("/") 
def hello_world():
    return "<p>Sab badiya</p>"

@app.get("/users")
def get_users():
    users = [user for user in db['users'].find()]
    return users
    
@app.post("/users")
def add_users():
    body = json.loads(request.data)
    email = db["users"].insert_one(body).inserted_id
    return email