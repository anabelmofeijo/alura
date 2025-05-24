from app.models.diagnosis_db import Diagnosis, AddDiagnosisDB
from app.models.patient_db import PatientProfile
from app import jsonify, datetime


class DiagnosisController:
    '''Diagnosis controller'''
    @staticmethod
    def get_diagnosis(id):
        try:
            datas = Diagnosis.query.filter(Diagnosis.patient_id==id).all()
            result = []
            if not datas:
                return jsonify({'message':'not found!'}), 400
            for data in datas:
                # print data from patient
                result.append(
                    {
                        'patient_id': data.patient_id,
                        'model_result': data.model_result,
                        'manchester_severity': data.manchester_severity
                    }
                )
                return jsonify(result), 200
            
        except Exception as e:
            return jsonify({'message': str(e)}), 500
        
    @staticmethod
    def post_diagnosis_controller(data):
        patient_id = data.get('patient_id')
        model_result = data.get('model_result')
        manchester_severity = data.get('manchester_severity')
        diagnosed_at = datetime.now()
        db = AddDiagnosisDB(patient_id=patient_id, model_result=model_result,manchester_severity=manchester_severity,diagnosed_at=diagnosed_at)
        
        response = db.add_diagnosis()

        return response
            
            