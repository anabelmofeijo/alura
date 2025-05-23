from app import db, datetime, jsonify, app, db

class Diagnosis(db.Model):
    # Diagnosis Model to database
    __tablename__ = 'diagnosis'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient_profile.id'), nullable=False)

    model_result = db.Column(db.JSON)
    manchester_severity = db.Column(db.String)
    diagnosed_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Diagnosis {self.id}>"
    
class AddDiagnosisDB:

    def __init__(self, patient_id, model_result, manchester_severity, diagnosed_at):
        self.patient_id = patient_id
        self.model_result = model_result
        self.manchester_severity = manchester_severity
        self.diagnosed_at = diagnosed_at

    def add_diagnosis(self):
        with app.app_context():
            try:
                print ('Trying to add diagnosis in database')
                diagnosis = Diagnosis(
                    patient_id = self.patient_id,
                    model_result = self.model_result,
                    manchester_severity = self.manchester_severity,
                    diagnosed_at =  self.diagnosed_at
                )

                db.session.add(diagnosis)
                db.session.commit()
                
                return jsonify({'message':'Diagnosis Added successfully'}), 200
            
            except Exception as e:
                return jsonify(
                    {
                        'message': str(e)
                    }
                ), 500
