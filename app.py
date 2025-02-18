from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello , prashanth"

@app.route("/profile" ,methods = ['post','get'])
def profile():
    if request.method == 'post':
        return "hello"
    else :
        return "get me here"

@app.route("/templete/<name>")
def templet_render():
    return render_template('hello.html',person = prasahnth)

if __name__=="__main__":
    app.run(debug=True)