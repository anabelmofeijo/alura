from app.controllers.auth_controller import AuthController
from app.models.user_db import AddUserDB, User
from app import app, jsonify, request

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

@app.route('/hospital/register/', methods=['POST'])
def hospital_registed():
    data = request.get_json()

    if not data:
        error_response = jsonify({'message':'fild everything'}), 400
        return error_response

    response = AuthController.register_hospital(data=data)
    return response