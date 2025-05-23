from app.models.diagnosis_db import Diagnosis
from app.models.patient_db import PatientProfile
from app import jsonify


class DiagnosisController:
    '''Diagnosis controller'''
    @staticmethod
    def get_diagnosis(id):
        datas = Diagnosis.query.filter(Diagnosis.patient_id==id).all()
        result = []
        if not datas:
            return jsonify({'message':'not found!'}), 400
        for data in datas:
            # print data from patient
            result.append(
                {
                    'patient_id': data.patient_id,
                    'model_result': data.model_reult,
                    'manchester_severety': data.manchester_severety
                }
            )
            return jsonify(result), 200
           
        