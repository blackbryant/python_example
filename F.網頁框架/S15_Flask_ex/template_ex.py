#pip install flask
#基本架構
#執行: flask.exe --app .\template_ex.py --debug run
#
from flask import Flask
from flask import render_template
from datetime import datetime
import pandas as pd

app = Flask(__name__)
app.debug = True
app.secret_key = '887-966-382'

df = pd.DataFrame({'國文':{'王小明':65,'李小美':80,'陳大同':55},
                    '英文':{'王小明':90,'李小美':90,'陳大同':72},
                    '數學':{'王小明':50,'李小美':66,'陳大同':89},
                    '自然':{'王小明':80,'李小美':65,'陳大同':79},
                    '社會':{'王小明':78,'李小美':70,'陳大同':55}
                    })


@app.route('/hello/<string:name>')
def hello(name):
    now= datetime.now()
    return render_template("hello.html",**locals())
 
#Template語言
#
@app.route("/var")
def variable():
  index_list=['王小明','李小美']
  column_list=['國文','英文']
  list = df.loc[['王小明','李小美'],['國文','英文']]

  return render_template("score.html",**locals())
 


if __name__=='__name__':
    app.run()


