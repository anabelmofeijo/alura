from app.models.user_db import AddUserDB
from app import app, jsonify, request, db
from app.models import User
from app import datetime


class AuthController:
    '''# configuration
    def __init__(self,name, email, password ):
        self.name = name
        self.email = email
        self.password = password
        self.date = datetime.now
        self.role = 'Patient'

    # add user in database
    def add_user(self):
        user = AddUserDB (
            name=self.name,
            email=self.email,
            password=self.password,
            role=self.role,
            created_at=self.date
        )
        user.add_user_to_db()
'''
    # Existing user controller
    @staticmethod
    def verify_existing_user(email):
        user = AddUserDB.verify_existing_user(email)
        return user
    
    @staticmethod
    def register_user():
        try:
            data = request.get_json()
            __name = data.get('name')
            __email = data.get('email')
            __password = data.get('password')

            if not __email and __name and __password:
                return jsonify({'error':  'Fill everysingle fild, please'}), 400
            else:
                user = User(
                    name = __name,
                    email = __email,
                    password_hash = __password,
                    role = 'patient'
                ) 
                db.session.add(user)
                db.session.commit()
                return jsonify({'message':'Added successfully'}), 200
            
        except Exception as e:
            print (f'Erro: {e}')
        
    @staticmethod
    def validadate_login():
        # get data from user
        
        data = request.get_json()
        __name = data.get('name')
        __email = data.get('email')
        __password = data.get('password')

        # verify if every fild is completed
        if not __email and __name and __password:
            return jsonify({'error':  'Fill everysingle fild, please'}), 400
        else:
            # Verify if email and password are wrong
            user = User.query.filter(User.email==__email, User.password_hash == __password).first()

            if not user:
                return jsonify(
                    {
                        'message':'user not found'
                    }
                ), 400
            
            return jsonify(
                {
                    'message':'user found'
                }
            ), 200
            
            
            
