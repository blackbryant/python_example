
from flask import Flask, request, jsonify,abort
#import git, os
import os
from web import create_app

# 项目代码目录(相对于webhook.py这个脚本的路径)
code_dir = "./"

#app = Flask(__name__)

if __name__ == '__main__':
    print("BBBBBBBBBBBBBB")
    app = create_app('development')
    app.run(host='0.0.0.0', port=7070)