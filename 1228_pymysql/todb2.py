from flask import Flask ,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://admin:0000@127.0.0.1:5432/test'
db = SQLAlchemy(app)