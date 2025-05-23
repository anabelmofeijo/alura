from app.models.user_db import User
from app.models.patient_db import PatientProfile
from  app import jsonify

class HistoryController:

    @staticmethod
    def user_history():
        try:
            users = User.query.all()
            user_list = []

            for user in users:
                user_list.append(
                    {
                        'name':user.name,
                        'email':user.email
                    }
                )
            return jsonify(user_list), 200
        
        except Exception as e:
            return jsonify({'message': str(e)}), 500
        
    @staticmethod
    def patient_history():
        try:
            patients = PatientProfile.query.all()
            response = []
            for patient in patients:
                response.append(
                    {
                        'patient_id' : patient.user_id,
                        'gender': patient.gender,
                        'height': patient.height,
                        'weight': patient.weight,
                        'pre_existing_conditions' : patient.pre_existing_conditions
                    }
                )
            return jsonify(response), 200
        
        except Exception as e:
            return jsonify({'message':str(e)}), 500
                
            

