from mongoengine import *

class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

new_service = Service(
    name = "Hera", 
    yob =1995,
    gender =0,
    height = 160,
    phone ="012345678",
    address = "Hanoi",
    status = True
) # tao ra document tu khuon service
new_service.save()