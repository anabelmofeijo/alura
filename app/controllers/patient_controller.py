from app.models.patient_db import PatientProfile, AddPatientProfileDB
from app import jsonify


class PatientController:
    # Put patient data in database
    @staticmethod
    def patient_profile(data):
        __age = data.get('age')
        __gender = data.get('gender')
        __height = data.get('height')
        __weight = data.get('weight')
        __conditions = data.get('pre_existing_conditions')

        db = AddPatientProfileDB(age=__age, gender=__gender, weight=__weight, height=__height, pre_existing_conditions=__conditions)
        db.add_patient_profile()

    @staticmethod
    def get_patiend_profile(id):
        db = AddPatientProfileDB()
        response = db.get_patient_profile_db(id)
        return response
