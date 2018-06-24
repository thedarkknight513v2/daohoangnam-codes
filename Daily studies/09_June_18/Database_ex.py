Basic database example

pip install pymongo
pip install gmail
https://api.mongodb.com/python/current/tutorial.html# 

from pymongo import MongoClient

mongo_uri = "mongodb://admin:superadmin1@ds253840.mlab.com:53840/c4e18-lab"

#1 connect database
client = MongoClient(mongo_uri)
# 2 get database
db = client.get_default_database()

# 3. Create collection
games = db["games"]

4. Create document
new_game = {
    "title": "PES",
    "description": "Pro evolution soccer"
}

5. Insert document
games.insert_one(new_game)

all_game = games.find()
for game in all_game:
    print(game)

