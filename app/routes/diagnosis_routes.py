from app.controllers.diagnosis_controller import DiagnosisController
from app import app


@app.route('/diagnosis/result/<int:id>', methods=['GET'])
def diagnosis(id):
    # Return Diagnosis from patient
    return DiagnosisController.get_diagnosis(id)