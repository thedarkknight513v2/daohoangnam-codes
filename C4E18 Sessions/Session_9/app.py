# fapp and tab (flask app)
from flask import Flask
app = Flask(__name__)

@app.route('/') #trang con, "/": vao trang chu
def index(): 
    return "Hello World"

@app.route("/hello")
def say_hello():
    return "Hello C4E18"
# Moi function va route fai 1 ten, khong duoc lap lai

@app.route("/nguoibencanh/<name>/<age>") #<parameters>
def say_hello_neighbor(name, age):
    return "Hi {0}, you are {1} years old".format(name,age) # request gui ve co bao nhieu parameters thi function fai co bang ay


# app run fai de cuoi cung
if __name__ == '__main__':  #khi ma file dc chay truc tiep thi se chay nhung gi trong nay
  app.run(debug=True)  # khoi dong server. Khi server co thay doi thi server se cap nhat ngay. code j thi cap nhat ngay



 