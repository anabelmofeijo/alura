from app import db, datetime, app, jsonify

class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Hospital {self.name}>'

class User(db.Model):
    # User model
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)  # 'patient' or 'doctor'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    profile = db.relationship('PatientProfile', backref='user', uselist=False)

    def __repr__(self):
        return f"<User {self.name}>"

class AddUserDB:
    # Class to add user
    def __init__(self, name, email, password, role, created_at):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.created_at = created_at

    # function to add a user in database
    def add_user_to_db(self):
        with app.app_context():
            try:
                print(f'Trying to add {self.email}')
                data = User(
                    name=self.name,
                    email=self.email,
                    password_hash=self.password,
                    role=self.role,
                    created_at=self.created_at
                )

                db.session.add(data)
                db.session.commit()
                print("added successfully!")

            except Exception as e:
                print(f'Erro ao adicionar usuário: {e}')
                db.session.rollback()

    # function to verify existing user
    @staticmethod
    def verify_existing_user(email):
        with app.app_context():
            data = User.query.filter(User.email==email).all()
            if data:
                return 'Found!', 200
            else:
                return 'Not found', 400
            
    @staticmethod
    def add_hospital(__name):
        try:
            hospital = Hospital.query.filter(Hospital.name==__name).all()
            if hospital:
                return jsonify({'message':'you are already in th sistem!'}), 400
            
            add = Hospital(name = __name)
            db.session.add(add)
            db.session.commit()

            return jsonify({'message':'hospital added succesfully!'}), 200
        
        except Exception as e:
            return jsonify({'message':str(e)}), 500
