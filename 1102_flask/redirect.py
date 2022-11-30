from flask import Flask,url_for,redirect
import time

app = Flask(__name__)

@app.route('/')
def test():
    print('start')
    time.sleep(2)
    return redirect(url_for('test1'))

@app.route('/test1')
def test1():
    print('this is test1')
    time.sleep(2)
    return redirect(url_for('test2'))

@app.route('/test2')
def test2():
    print('this is test2')
    time.sleep(2)
    return redirect(url_for('test3'))

@ app.route('/test3')
def test3():
    print('this is test3')
    time.sleep(2)
    return redirect('https://www.dcard.tw')

if __name__ == '__main__':
    app.run()