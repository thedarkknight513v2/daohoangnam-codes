import mongoengine
from mongoengine import *
from pymongo import MongoClient
mongo_uri = "mongodb://<dbuser>:<dbpassword>@ds117431.mlab.com:17431/muadongkhonglanh-final"
client = MongoClient(mongo_uri)
# 2 get database
db = client.get_default_database()

host = "ds117431.mlab.com"
port = 17431
db_name = "muadongkhonglanh-final"
user_name = "dhnam1993"
password = "dhnam1993"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())

class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

all_service = db.objects()

c= all_service.objects.get(id='5b2fad8c0cc1751600df7a6c')
print(c)