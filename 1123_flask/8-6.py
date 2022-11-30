from flask import Flask
app = Flask(__name__)

@app.route('/add/<int:number>')
def add_one(number):
    return '%d' %(number+1)
if __name__== '__main__':
    app.run()