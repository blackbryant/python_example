from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! change (from a Docker container)'

@app.route('/app')
def app_show():
    return 'App  d2234  change (from a Docker container)'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


