from app.models.patient_db import PatientProfile, AddPatientProfileDB
from app import jsonify, db


class PatientController:
    # Put patient data in database
    @staticmethod
    def patient_profile(data):
        try:
            __user_id = data.get('user_id')
            __age = data.get('age')
            __gender = data.get('gender')
            __height = data.get('height')
            __weight = data.get('weight')
            __conditions = data.get('pre_existing_conditions')

            patient = AddPatientProfileDB(user_id=__user_id,age=__age, gender=__gender, weight=__weight, height=__height, pre_existing_conditions=__conditions)
            patient_registered = patient.verify_existing_patient(__user_id)
            if patient_registered:
                return jsonify({
                    'message':"you are already registered"
                }), 400

            db = AddPatientProfileDB(user_id=__user_id,age=__age, gender=__gender, weight=__weight, height=__height, pre_existing_conditions=__conditions)
            response = db.add_patient_profile()

            if response:
                return jsonify(
                    {
                        "message":"Patient Profile Added Successfully!"
                    }
                ), 200

        except Exception as e:
            print(f'Erro: {e}')

    @staticmethod
    def get_patiend_profile(id):
        db = AddPatientProfileDB()
        response = db.get_patient_profile_db(id)
        return response
