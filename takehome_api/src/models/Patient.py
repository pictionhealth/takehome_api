from takehome_api.src.database import db


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # add additional fields as needed