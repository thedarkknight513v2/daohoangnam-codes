    XII_Web part I: Tạo server bằng local host

    Viet html: ! + tab

    from flask import Flask
    from flask import render_template

    app = Flask(__name__)

    Example 1: tạo trang chủ
    @app.route('/')
    def index():
        return "Hello World"

    Example 2: Tạo subpage của trang chủ
    @app.route("/hello")  
    def say_hello():
        return "Hello C4e18"

    Example 3: Tạo subpage dùng parameters (1/2)
    @app.route("/sayhitoneighbor/<name>/<age>")
    def hello_neighnot(name, age):
        return "Hi {0} you are {1} years old".format(name, age)

    example 4: Tạo subpage dùng parameters (2/2)
    @app.route("/yolo/<meaning>")
    def yolo(meaning):
        return "Its mean is" + meaning

    Example 5: Calculate SUM
    @app.route("/sum/<int:x>/<int:y>")
    def sum_calculate(x,y):
        return str(x + y)

    Example 6: Sử dụng html
    @app.route("/html")
    def html_ex():
        return "<h1>hello Nam</h1>"

    Example 7: Sử dụng html và lưu biến. Tao folder ten "templates"
    @app.route("/index")
    def html_ex2():
        post_title = "Thơ con ếch"  # bien ben html: post_title
        post_content = "Tiền không mang lại hạnh phúc cho những người không có chúng"
        post_author = "Dao Hoang Nam"
        return render_template("index.html", post_title = post_title, post_content = post_content, post_author = post_author)

    Example 8:  Sử dụng html và lưu biến. Server gửi nội dung sang html
    @app.route("/index2")
    def html_ex3():
        posts = [
        {
        "title": "Thơ con dế",  # bien ben html: post_title
        "content": "Hôm nay trăng lên cao tít",
        "author": "thedarkknight513",
        "gender": 1
        },

        {"title": "Thơ con mèo",  # bien ben html: post_title
        "content": "Nếu tiền không làm bạn hạnh phúc thì hãy đưa nó cho tôi",
        "author": "Nathan Drake",
        "gender": 0
        },

        {"title": "Thơ con dế",  # bien ben html: post_title
        "content": "Đề thi vừa sức với các bạn và quá sức với em",
        "author": "python",
        "gender": 1
        }
        ]

        first_post = posts[1]
        C1:post là biến gửi sang html. Python thấy render template thì tự vào folder templates tìm 
        return render_template("index.html", post = first_post) 
        C2: 
        return render_template("index.html", posts = posts)

        Bên TAB HTML:
        <body>
        {% for p in posts %}
        <h1>hello from the other side</h1>
        <h3>
            {{ p.title }}
        </h3>
        <p>
            {{ p.content}} 
        </p>
        <i>
            by: 
            {% if p.gender == 1 %} 
            Mr.
            {% elif p.gender ==0 %} 
            Ms.
            {% endif %}
            {{ p.author}} 
        {% endfor %}
        </body>

    Luôn để run app ở cuối cùng
    if __name__ == '__main__':
    app.run(debug=True)