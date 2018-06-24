import mongoengine
# mongodb://namdh1993:namdh1993@ds263520.mlab.com:63520/muadongkhonglanh-c4e18

host = "ds263520.mlab.com"
port = 63520
db_name = "muadongkhonglanh-c4e18"
user_name = "namdh1993"
password = "namdh1993"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())