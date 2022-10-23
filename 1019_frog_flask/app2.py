from flask import Flask

app = Flask(__name__)
@app.route("/") #根目錄
@app.route("/idandname")
def hello():
    return "C110156217 趙伯恩"

@app.route("/test")
def test():
    return "<h1>ok打ok  ok<h1>"
if __name__ == "__main__":
    app.run(host='127.0.0.1',port='8080')