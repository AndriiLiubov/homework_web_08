import os

from mongoengine import connect
from dotenv import load_dotenv


load_dotenv()

MONGO_PASS = os.getenv("MONGO_PASS")
URI = f"mongodb+srv://andriiliubov:{MONGO_PASS}@cluster0.exgrzep.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

connect(host=URI, db = "Poets")