from . import db



class Vote(db.Model):
    __tablename__='votes'
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(60))


class CapWeight(db.Model):
    __tablename__='capweight'
    id = db.Column(db.Integer, primary_key=True)
    capacity = db.Column(db.Integer)

class ItemWeight(db.Model):
    __tablename__='itemweight'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.Integer)







