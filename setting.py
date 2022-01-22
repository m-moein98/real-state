from bson.objectid import ObjectId
from pymongo import MongoClient

# Hash Algorythm
SECRET_KEY = "427d2a8539281bac983ec2da6f0ba910f661eb19f3a2edd693457250736c0548"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# DB Setting
host = "localhost"
collection_name = "Ireen"
db_name = "Ireen-db"
username = "root"
password = "KjbkERFQTYrlcLyyE7ygYiau"
client = MongoClient("arthur.iran.liara.ir", 32526, username=username, password=password)
db = client.Ireen
link_collection = db.Listing
user_collection = db.User
token_collection = db.Token
