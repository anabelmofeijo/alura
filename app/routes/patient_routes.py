from app.controllers.patient_controller import PatientController
from app import app, request


@app.route('/patient/profile/', methods = ['POST'])
def patient_profile():
    # route to post patient basic data
    ''''
    json model to post something about patient
    {
        "user_id":""
        "age":"",
        "gender":"",
        "height":"",
        "weight":"",
        "pre_existing_conditions":""
    }
    '''
    data = request.get_json()
    patient = PatientController()
    result = patient.patient_profile(data)
    return result

@app.route('/patient/profile/<int:id>', methods=['GET'])
def get_patient_profile(id):
    data = PatientController()
    response = data.get_patiend_profile(id=id)
    return response