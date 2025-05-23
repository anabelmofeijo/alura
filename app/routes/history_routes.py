from app.controllers.history_controller import HistoryController
from app import app


@app.route('/history/patients/', methods=['GET'])
def history_patient():
    history = HistoryController()
    response = history.patient_history()
    return response

@app.route('/history/users/', methods=['GET'])
def history_users ():
    history = HistoryController()
    response = history.user_history()
    return response