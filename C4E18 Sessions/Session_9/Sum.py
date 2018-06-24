# fapp and tab (flask app)
from jinja2 import Template
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #trang con, "/": vao trang chu
def index(): 
    # title = "Tho con coc"
    return "Hello World"

# @app.route("/hello")
# def say_hello():
#     return "<h1>Hello World</h1>"

@app.route("/hello")
def say_hello():
    posts =[
        {
    "post_title": "Tho con ech",
    "post_content" : "YOLO",
    "post_author" : "Dao Hoang Nam",
    "gender": 1
        },
        {"post_title": "b",
        "post_content": "d",
        "post_author": "e",
        "gender": 1
        },
        {"post_title": "f",
        "post_content": "h",
        "post_author": "abc",
        "gender": 0
        }
    ]

    first_post = posts[0]
    # post_title = "Tho con ech"
    # post_content = "YOLO"
    # post_author = "Dao Hoang Nam"
    
    # return render_template("index.html", post_title = post_title, post_author = post_author, post_content= post_content)  # cau truc cua server flask: fai de vao trong 1 folder templates
    return render_template("index.html", posts = posts)  # cau truc cua server flask: fai de vao trong 1 folder templates


# Moi function va route fai 1 ten, khong duoc lap lai

@app.route("/sum/<int:x>/<int:y>") #<parameters>
def say_hello_neighbor(x, y):
    # total = int(x) + int(y)
    total = x + y
    return "The total is {0}".format(total) # request gui ve co bao nhieu parameters thi function fai co bang ay

if __name__ == '__main__':  #khi ma file dc chay truc tiep thi se chay nhung gi trong nay
  app.run(debug=True)  # khoi dong server. Khi server co thay doi thi server se cap nhat ngay. code j thi cap nhat ngay. host: dia chi serve, port: duong vao server. domain = host + port
# 127.0.0.1: dia chi may cua minh (local host)


 