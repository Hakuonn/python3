from flask import Flask

app = Flask(__name__)

@app.route('/school/')
def schools():
    return 'the school page'

@app.route('/student')
def stuents():
    return 'the students page'

if __name__ == '__main__':
    app.run(debug=True)