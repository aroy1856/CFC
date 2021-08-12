from db import db

class UserModel(db.Model):
    __tablename__ = 'User'

    Id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    PhoneNumber = db.Column(db.Integer)
    Email = db.Column(db.String(50))
    Password = db.Column(db.String(20))
    FirstLineOfAddress = db.Column(db.String(30))
    Street = db.Column(db.String(20))
    Area = db.Column(db.String(30))
    District = db.Column(db.String(20))
    Pincode = db.Column(db.Integer)

    def __init__(self, email, fname, lname, number, password, fladdress, street, area, district, pincode):
        self.Email = email
        self.FirstName = fname
        self.LastName = lname
        self.PhoneNumber = number
        self.Password = password
        self.FirstLineOfAddress = fladdress
        self.Street = street
        self.Area = area
        self.District = district
        self.Pincode = pincode

    @property
    def json(self):
        return {
            'firstname': self.FirstName,
            'lastname': self.LastName,
            'phonenumber': self.PhoneNumber,
            'email': self.Email,
            'firstlineofaddress': self.FirstLineOfAddress,
            'street': self.Street,
            'area': self.Area,
            'district': self.District,
            'pincode': self.Pincode
        }

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(Email=email).first()