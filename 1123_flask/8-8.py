from flask import Flask

app = Flask(__name__)

@app.route('/message' , methods=['POST'])
def fo_send():
    return 'this is for post method'

@app.route('/message' , methods=['GET'])
def show_the_send_from():
    return 'this is for get method'

if __name__ == '__main__':
    app.run()