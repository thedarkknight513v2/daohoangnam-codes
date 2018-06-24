from flask import Flask, render_template
import mlab
from models.service import Service

app = Flask(__name__)
print("a")
# 0. Create connection
mlab.connect()

# 1. Design database
# Service: collection, class : document. Document: 1 module trong mongoengine


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)


 