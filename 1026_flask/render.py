from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def text():
    return "<html><body><h1>Hello World</h1><p>\
        <h3>test</h3>\
        <h1><b><i>AAAAAAAAAAA</i></b></h1></body></html>"

@app.route('/home')
def home():
    return render_template('home.html') 

@app.route('/page/text')
def pageText():
    return render_template('page.html',text='C110156217 趙伯恩') 

@app.route('/page/app')
def pageAppInfo():
    appInfo = {
        'id':5,
        'name':'Python-Flask',
        'Version':'3.7.10',
        'remark':'Python Web Framework'
    }
    return render_template('page.html',appInfo=appInfo) 

@app.route('/page/intro')
def introInfo():
    intro = {
        'id':'C110156217',
        'name':'趙伯恩',
        'birth':'2003/02',
        'interest':'7tou',
        'expertise':'program'
    }
    return render_template('page.html',introInfo=intro)

@app.route('/page/data')
def pageData():
    data = {
        'Tesla':'ModelY',
        'BMW':'ModelY',
        'Tesla3':'X3',
        'Toyota':'RAV4',
        '勞斯萊斯':'Rolls-Royce Ghost',
        'Benz':'C300',
    }
    return render_template('page.html',data=data)

@app.route('/static')
def staticPage():
    return render_template('static.html')

if __name__ == "__main__":
    app.run()