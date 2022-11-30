from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

@app.route('/form')
def formPage():
    return render_template('Form.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        number = request.form['number']
        number = int(number)
        if number == 2:
            return '2是質數'
        elif number == 1 :
            return '1不是質數'
        else:
            for i in range(2,number):
                if number%i == 0:
                    return '%d不是質數' %(number)
                else:
                    return '%d是質數' %(number)
        return redirect(url_for('success',name=number,action='post'))
    else:
        number = request.args.get('number')
        number = int(number)
        if number == 2:
            return '2是質數'
        elif number == 1 :
            return '1不是質數'
        else:
            for i in range(2,number):
                if number%i == 0:
                    return '%d不是質數' %(number)
                else:
                    return '%d是質數' %(number)
        return redirect(url_for('success',name=number,action='get'))
@app.route('/success/<action>/<number>')
def success(name,action):
    return '{} : Welcome {}'.format(action,name)

if __name__ == '__main__':
    app.run(debug=True)