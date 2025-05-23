from app.controllers.auth_controller import AuthController
from app.models.user_db import AddUserDB, User
from app import app, jsonify

#home
@app.route('/')
def home():
    message = jsonify (
        {
            'message':'api is running'
        }
    )
    return message

# route to register the user
@app.route('/auth/register/', methods=['POST'])
def register():
    data = AuthController()
    response = data.register_user()
    return response

# route to login the user
@app.route('/auth/login/', methods=['POST'])
def login():
    data = AuthController()
    response = data.validadate_login()
    return response
