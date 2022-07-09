import datetime
import re

from sqlalchemy.orm import validates
from sqlalchemy import desc, func

from . import db


class LicensePlate(db.Model):
    
    __tablename__ = 'license_plates'

    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(10), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)


    @property
    def timestamp(self):
        return self.created_at.strftime('%Y-%m-%dT%H:%M:%SZ')
    
    @validates('plate')
    def validate_plate(self, key, value):
        match = re.search("^[A-Z]{1,3}-[A-Z]{1,2}[1-9]\d{0,3}$", value)
        assert match, f"invalid '{key}' No: {value}"
        return value

    @classmethod
    def add(cls, plate):
        """
        Add plate

        Positional arguments:
        plate -- string
        """
        obj = LicensePlate(plate = plate)
        db.session.add(obj)
        db.session.commit()

        return obj


    @classmethod
    def search(cls, key, levenshtein):
        """
        Search plate

        Positional arguments:
        key -- string
        levenshtein -- int
        """
        
        cond = func.levenshtein(func.Replace(LicensePlate.plate, '-', ''), key)

        licence_plates = LicensePlate.query.filter(cond <= levenshtein).order_by(cond).all()

        return licence_plates

    