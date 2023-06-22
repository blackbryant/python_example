#pip install flask
#基本架構
#執行: flask --app  route_ex.py run
#
from flask import Flask
app = Flask(__name__)

CONFIGS = {
    "ENV": "development",
    "DEBUG": True
}

#多路由對應相同函示
@app.route("/")
@app.route("/index")
def index():
    return "index"

#單一路由
@app.route('/hello')

def hello():
    return 'hello'

#路由傳遞參數
#string/int/float
@app.route("/hello/<name>")
def hello2(name):
    return "Hi! {}".format(name)


if __name__=='__name__':
    app.run()


