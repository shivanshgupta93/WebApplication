from sqlalchemy import Column, Integer, String, Date
from models.base import Base
import datetime

#### Country class to create Country table
class Country(Base):
    __tablename__ = 'country'

    country_id = Column(Integer, primary_key=True)
    country_name = Column(String)
    inserted_date = Column(Date(), default=datetime.datetime.now().date())

    def __repr__(self):
        return "<Country (country_id='%d', country_name='%s', inserted_date='%s' )" % (self.country_id, self.country_name, self.inserted_date)
