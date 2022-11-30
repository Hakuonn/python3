from flask import Flask
app = Flask(__name__)

@app.route('/add/<int:number>')
def add_one(number):
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
if __name__== '__main__':
    app.run()


#改成質數判斷
