from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Configuration SQLalchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration JWT
app.config['SECRET_KEY'] = 'your_strong_secret_key'
app.config["JWT_SECRET_KEY"] = 'your_jwt_secret_key'
app.config['JWT_TOKEN_LOCATION'] = ['headers']

# database inicialization
db = SQLAlchemy(app)

# JWT Initialization
jwt = JWTManager(app)

# cors
CORS(app)

# create database
def create_database():
   with app.app_context():
      db.create_all()
