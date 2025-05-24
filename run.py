from app.routes import auth_routes, diagnosis_routes, symptoms_routes
from app.routes import auth_routes, patient_routes, history_routes
from app import app


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host="0.0.0.0", port=5000)
