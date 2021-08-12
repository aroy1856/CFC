from db import db


class ItemModel(db.Model):
    __tablename__ = 'Student'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(20))
    # price = db.Column(db.Float(precision=2))

    def __init__(self, name, s_id):
        self.Name = name
        self.Id = s_id

    def json(self):
        return {'name': self.Name, 'price': self.Id}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()