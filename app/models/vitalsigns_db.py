from app import db, datetime

class VitalSigns(db.Model):
    # Vital Signs Model to database
    __tablename__ = 'vital_signs'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient_profile.id'), nullable=False)

    bpm = db.Column(db.Integer)
    spo2 = db.Column(db.Float)
    temperature = db.Column(db.Float)
    ecg = db.Column(db.String)

    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<VitalSigns {self.id}>"