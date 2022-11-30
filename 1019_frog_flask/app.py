from flask import Flask

app = Flask(__name__)
@app.route("/") #根目錄
def hello():
    return "C110156217 趙伯恩"
if __name__ == "__main__":
    app.run()