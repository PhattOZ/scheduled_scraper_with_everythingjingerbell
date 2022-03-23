import os
import time
import datetime
import certifi
import schedule
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URL"), tlsCAFile = certifi.where())

db = client.learn_python

def query():
    print(db.my_collection.insert_one({"inserted on": datetime.date.today()}))

def log():
    print('logging' + str(datetime.date.today()))

schedule.every(10).seconds.do(log)
# schedule.every(20).seconds.do(query)

while True:
    schedule.run_pending()
    time.sleep(1)