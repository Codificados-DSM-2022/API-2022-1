from flask import Flask, render_template, request
from routes.solicitar import solicitar
from routes.solicitar import solicitarExec
from flask_sqlalchemy import SQLAlchemy
#from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:tuca123@localhost/projeto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(solicitar)
app.register_blueprint(solicitarExec)