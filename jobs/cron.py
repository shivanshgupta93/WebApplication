import os
import requests
from consts import *
from db import DB
from models.institutions import Institution
from models.countries import Country
from middlewares.deserializer import deserializer

db_obj = DB() ### creating a object of DB function in db.py file
db_session = db_obj.get_db() ### getting a session of database

run_cron = int(os.environ.get("run_cron_job", 0))  #### getting cron job environment variable, by default not to run the database data load

def cron_job(run_cron):
    if run_cron == 1:
        for key,value in EDUCATION.items():
            top = deserializer(requests.get(BASE_URL+"/"+value)) ### getting data from Client API URL
                        
            if key == "countries": ### inserting country data into table
                db_session.add_all(
                [Country(country_id=int(next_item['id']), country_name=next_item.get('name', 'None'))
                for next_item in top]
                )
                db_session.commit()
                

            if key == "institutions": ### inserting institutions data into table
                db_session.add_all(
                [Institution(institution_id=int(next_item['id']), institution_name=next_item.get('name', 'None'), city_id=int(next_item.get('city_id', 0)), city_name=next_item['city'].get('name','None'),
                country_id=int(next_item['country_id']), course_count=int(next_item.get('course_count',0)))
                for next_item in top]
                )
                db_session.commit()

def add_country(item): ### inserting single countries details into table
    db_session.add_all(
                    [Country(country_id=int(item['country_id']), country_name=item.get('country_name', 'None'))]
                    )
    db_session.commit()

def add_institution(item): ### inserting single institution details into table
    db_session.add_all(
                    [Institution(institution_id=int(item['institution_id']), institution_name=item.get('institution_name', 'None'), city_id=int(item.get('city_id', 0)), city_name=item.get('city_name','None'),
                    country_id=int(item['country_id']), course_count=int(item.get('course_count',0)))]
                    )
    db_session.commit()
