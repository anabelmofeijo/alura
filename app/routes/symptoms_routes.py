from app.controllers.symptoms_controller import SymptomController
from app import app, request

# submit symptoms in database
@app.route('/symptoms/submit/', methods=['POST'])
def symptoms():
    data = request.get_json()
    symp = SymptomController()
    result = symp.post_symptoms(data)
    return result

# Return a symptom from a specific patient
@app.route('/symptoms/patient/<int:id>', methods=['GET'])
def get_symptoms(id):
    data = SymptomController()
    response = data.get_symptoms(id=id)
    return response