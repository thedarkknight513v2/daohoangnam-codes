from flask import Flask, render_template, redirect, url_for, request
import mlab
import mlab2hw
from models.service import Service 
from models.customer import Customer
from mongoengine import *
app = Flask(__name__)

#0. Create connection
mlab.connect()
mlab2hw.connect()


# Day object/document len database

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/search")
def search1():
    # day thong tin service len day. lay thong tin tu database
    all_service = Service.objects(gender = gender) #lay ra document trong Service thoa man tieu chi
    return render_template("search.html", all_service = all_service)


@app.route("/search/<gender>")
def search2(gender):
    # day thong tin service len day. lay thong tin tu database
    # all_service = Service.objects(gender = gender, yob__lte =1998,address__icontains="Hanoi") #lay ra document trong Service thoa man tieu chi
    all_service = Service.objects(gender = gender) #lay ra document trong Service thoa man tieu chi
    return render_template("search.html", all_service = all_service)


@app.route("/customer")
def customer():
    all_customer = Customer.objects()
    return render_template("customer.html", all_customer = all_customer)
    # return all_customer[1]

@app.route("/customer2")
def customer_2():
    all_customer = Customer.objects(contracted = False)
    ten_customer = all_customer[0:10]
    return render_template("customer.html",ten_customer = ten_customer)

@app.route("/admin")
def admin():
    all_service = Service.objects()
    return render_template("admin.html", all_service = all_service)


@app.route("/admin/delete/<service_id>")
def delete(service_id):
    # return render_template("delete.html")
    service_to_delete = Service.objects().with_id(service_id) 
    if service_to_delete is None:
        return "Service not found"
    else:
        service_to_delete.delete()
        # return "deleted" + service_id
        return redirect(url_for("admin"))

@app.route("/admin/new_service", methods = ["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("new_service.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        address = form["address"]

        new_service = Service(
            name = name,
            yob = yob,
            address = address
        )
        new_service.save()

        return redirect(url_for("admin"))

if __name__ == '__main__':
  app.run(debug=True)   
 