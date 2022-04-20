
from sqlalchemy.orm import relationship
from app import db

# Definign User model for users table
class User(db.Model):
   __tablename__ = 'users'

   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String, nullable=False)
   password = db.Column(db.String, unique=True, nullable=False)
   

# Definign Car model for cars table
class Car(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    object_id = db.Column(db.String(), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=True, nullable=False)
    make = db.Column(db.String(), nullable=False)
    model = db.Column(db.String(), nullable=False)
    category = db.Column(db.String(), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    owner = relationship("User")
    # Conversion of data of the cars model to show on frontend
    def to_json(self):
        return {
            "id":self.id,
            "object_id":self.object_id,
            "year":self.year,
            "make": self.make,
            "model": self.model,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            
        }   

       