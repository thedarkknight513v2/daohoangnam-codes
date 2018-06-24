from mongoengine import *

#1. Design database
class Service(Document):
    name = StringField()
    dob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

