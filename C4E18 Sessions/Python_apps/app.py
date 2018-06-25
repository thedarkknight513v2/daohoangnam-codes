from flask import Flask, render_template
import mlab
from models.service import Service 
# from mongoengine import *
app = Flask(__name__)

#0. Create connection
mlab.connect()


# Day object/document len database

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/search")
def search1():
    # day thong tin service len day. lay thong tin tu database
    all_service = Service.objects(gender = 1) #lay ra document trong Service thoa man tieu chi
    return render_template("search.html", all_service = all_service)


@app.route("/search/<gender>")
def search2(gender):
    # day thong tin service len day. lay thong tin tu database
    all_service = Service.objects(gender = gender, yob__lte =1998,address__icontains="Hanoi") #lay ra document trong Service thoa man tieu chi
    return render_template("search.html", all_service = all_service)

 



if __name__ == '__main__':
  app.run(debug=True)   
 