#pip install flask
#
#
from flask import Flask
app = Flask(__name__)



@app.route("/")
@app.route('/hello')

def hello():
    return 'hello'

def index():
    return "home"



if __name__=='__name__':
    app.run()


