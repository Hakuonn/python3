from flask import Flask,session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'SET_ME_BEFORE_USE_SEESION'

@app.route('/write_session')
def writesession():
    session['key_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return session['key_time']

@app.route('/read_session')
def readsession():
    return session.get('key_time') or "None"
if __name__ == '__main__':
    app.run(debug=True)