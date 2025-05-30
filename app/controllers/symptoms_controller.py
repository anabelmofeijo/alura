from app.models.symptoms_db import AddSymptomsDB
from app import request, jsonify, datetime


class SymptomController():

    # post symptoms
    @staticmethod
    def post_symptoms(data):
        symptoms = data.get('values', [])
        patient_id = data.get('patient_id')
        recorded_at = datetime.now()

        db = AddSymptomsDB(symptom_list=symptoms, patient_id=patient_id, recorded_at=recorded_at)
        if db:
            db.add_symptom()
        else:
            return jsonify(
                {
                    'message':'symptoms not submited'
                }
            ), 400

        return jsonify(
            {
                'message':'symptoms, submited successfully'
            }
        ), 200
    
    @staticmethod
    def get_symptoms(id):
        response = AddSymptomsDB.get_symptoms_db(id)
        return response

