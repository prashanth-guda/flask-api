from flask import Flask

app = Flask(__name__)

@app.route("/login")
def hello():
    return "hello , prashanth!"


@app.route("/")
def homepage():
    return "this is a home page"



if __name__=="__main__":
    app.run(debug=True)