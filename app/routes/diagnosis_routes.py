from app.controllers.diagnosis_controller import DiagnosisController
from app import app, jsonify, request


@app.route('/diagnosis/result/<int:id>', methods=['GET'])
def diagnosis(id):
    # Return Diagnosis from patient
    response = DiagnosisController.get_diagnosis(id)
    if not response:
        return jsonify({'message':'your diagnosis is not ready!'}), 400
    
    return response

@app.route('/diagnosis/post/', methods = ['POST'])
def post_diagnosis():
    data = request.get_json()
    diagnosis = DiagnosisController()
    response = diagnosis.post_diagnosis_controller(data=data)
    return response