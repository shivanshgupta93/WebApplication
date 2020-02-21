from sqlalchemy import Column, Integer, String, Date
from models.base import Base
import datetime

#### Institution class to create Institution table
class Institution(Base):
    __tablename__ = 'institutions'

    institution_id = Column(Integer, primary_key=True)
    institution_name = Column(String)
    city_id = Column(Integer)
    city_name = Column(String)
    country_id = Column(Integer)
    course_count = Column(Integer)
    inserted_date = Column(Date(), default=datetime.datetime.now().date())

    def __repr__(self):
        return "<Institution (institution_id='%d', institution_name='%s', city_id='%d', city_name='%s', country_id='%d', course_count='%d', inserted_date='%s' )" % (self.institution_id, self.institution_name, self.city_id, self.city_name, self.country_id, self.course_count, self.inserted_date)
