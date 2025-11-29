from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ashwathbala0510_db_user:<password>@cluster0.qlbtjjd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Creating a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Sending a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)