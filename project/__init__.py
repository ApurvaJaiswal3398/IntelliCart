from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import pymongo
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8946d71d0200e86083be400cb72e4700'
app.config['UPLOAD_FOLDER']=os.path.join(os.getcwd(),"project/static/profile_pics/").replace("\\",'/')

crypt = Bcrypt(app)

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection["Supermarket_Database"]
Users = db["Users"]
Carts = db["Carts"]
Products = db["Products"]
Customer_Cart = db["Customer_Cart"]
Billing = db["Billing"]

from project import routes