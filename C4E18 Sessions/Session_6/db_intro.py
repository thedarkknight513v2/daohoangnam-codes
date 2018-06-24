# pip install pymongo
# pip install gmail
# https://api.mongodb.com/python/current/tutorial.html

from pymongo import MongoClient

mongo_uri = "mongodb://namdh1993:namdh1993@ds151840.mlab.com:51840/lab-c4e18"
#1. Connect to database
client = MongoClient(mongo_uri)

#2. Get database
db = client.get_default_database()

#3. Create collection
games = db["games"]
# db la dictionary

#4. Create document
# new_game = {
#     "title": "LOL",
#     "description": "League of legends"
# }

#5. insert document into collection
# games.insert_one(new_game)
# collection.insert_one(document)

all_game = games.find()

for game in all_game:
    print(game)

