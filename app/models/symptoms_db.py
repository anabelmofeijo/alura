from app import db, app, datetime, jsonify


class Symptoms(db.Model):
    # Symptom Model to database
    __tablename__ = 'symptoms'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient_profile.id'), nullable=False)
    symptom_list = db.Column(db.JSON) 
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Symptoms {self.id}>"
    

class AddSymptomsDB:
    def __init__(self, symptom_list, recorded_at, patient_id):
        self.symptom_list = symptom_list
        self.recorded_at = recorded_at
        self.patient_id = patient_id

    def add_symptom(self):
        with app.app_context():
            try:
                print ('Trying to add symptoms in database')
                data = Symptoms(
                    patient_id = self.patient_id,
                    symptom_list = self.symptom_list,
                    recorded_at = self.recorded_at
                )

                db.session.add(data)
                db.session.commit()
                print("added successfully!")

            except Exception as e:
                print (f'Erro: {e}')


    def get_symptoms_db(id):
        datas = Symptoms.query.filter(Symptoms.patient_id==id).all()
        result = []

        if not datas:
            return jsonify ( {
                    'message':'not found'
                }
            ), 200
        
        for data in datas:
            result.append(
                {
                    'patient_id': data.patient_id,
                    'symptom_list': data.symptom_list,
                    'recorded_at': data.recorded_at
                }
            ), 200


