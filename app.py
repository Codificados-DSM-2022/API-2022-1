from flask import Flask, render_template, request
from routes.solicitar import solicitar
from flask_sqlalchemy import SQLAlchemy
#from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:tuca123@localhost/api'
app.config['SQLALBHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(solicitar)