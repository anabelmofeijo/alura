from app import app, db, jsonify

class PatientProfile(db.Model):
    # Patient Profile - Model to database
    __tablename__ = 'patient_profile'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    pre_existing_conditions = db.Column(db.Text)

    vital_signs = db.relationship('VitalSigns', backref='patient', lazy=True)
    symptoms = db.relationship('Symptoms', backref='patient', lazy=True)
    diagnoses = db.relationship('Diagnosis', backref='patient', lazy=True)

    def __repr__(self):
        return f"<PatientProfile of {self.user.name}>"
    

class AddPatientProfileDB:
    # class to add patient in database
    def __init__(self, user_id,age, gender, weight, height, pre_existing_conditions):
        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.pre_existing_conditions = pre_existing_conditions

    def add_patient_profile(self):
        # the function to add a patient in database
        with app.app_context():
            try:
                print ('Trying to add patient profile')
                data = PatientProfile(
                    user_id = self.user_id,
                    age = self.age,
                    gender = self.gender,
                    weight = self.weight,
                    height = self.height,
                    pre_existing_conditions = self.pre_existing_conditions
                )

                db.session.add(data)
                db.session.commit()
                return 'added successfully!'
                
            except Exception as e:
                print (f'Erro: {e}')

    # Return patient profile
    @staticmethod
    def get_patient_profile_db(id):
        # A function to return an specif patient in database
        datas = PatientProfile.query.filter(PatientProfile.user_id==id).all()
        result = []

        if not datas:
            return jsonify (
                {
                    'message':'patient not found'
                }
            ), 400
        
        for data in datas:
            result.append(
                {
                    'patient_id' : data.patient_id,
                    'gender': data.gender,
                    'height': data.height,
                    'weight': data.weight,
                    'pre_existing_conditions' : data.pre_existing_conditions
                }
            ), 200

    @staticmethod
    def verify_existing_patient(id):
        datas = PatientProfile.query.filter(PatientProfile.user_id==id).all()

        if datas:
            return jsonify (
                {
                    'message':'your already registered in patient profile'
                }
            ), 400