from app import app

@app.route('/patient/history/')
def patient_history():
    return 'list history'

@app.route('/patient/history/id')
def patient_history_id():
    return 'patient_history_id'