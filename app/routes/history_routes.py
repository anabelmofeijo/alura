from app.controllers.history_controller import HistoryController
from app import app

# list every patient in database
@app.route('/history/patients/', methods=['GET'])
def history_patient():
    history = HistoryController()
    response = history.patient_history()
    return response

# list every single user in database
@app.route('/history/users/', methods=['GET'])
def history_users ():
    history = HistoryController()
    response = history.user_history()
    return response