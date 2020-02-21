from flask import Blueprint, request
from db import DB
from models.countries import Country
from models.institutions import Institution
from middlewares.serializer import serialize
from jobs.cron import add_institution, add_country
import datetime

db_obj = DB() ### creating a object of DB function in db.py file
db_session = db_obj.get_db() ### getting a session of database

api = Blueprint("api", __name__, url_prefix="/api")

### GET RestAPI for institution details
@api.route("/institutions", methods = ['GET'])
def institutions():
    institution = db_session.query(Institution).all()
    return serialize(institution)

### GET RestAPI for countries details
@api.route("/countries", methods = ['GET'])
def countries():
    country = db_session.query(Country).all()
    return serialize(country)

### GET RestAPI for a countries detail, passed with country_id
@api.route("/countries/<int:country_id>", methods = ['GET'])
def countries_filter(country_id):
    country = db_session.query(Country).filter(Country.country_id == country_id)
    return serialize(country)

### GET RestAPI for a institution detail, passed with institution_id
@api.route("/institutions/<int:institution_id>", methods = ['GET'])
def institutions_filter(institution_id):
    institution = db_session.query(Institution).filter( Institution.institution_id == institution_id)
    return serialize(institution)

### Post API for add new institution with or without adding country
@api.route("/institutions", methods = ['POST'])
def create_institution():
    input_data = request.json
    country_id = request.json['country_id']
    country_data = serialize(db_session.query(Country).filter(Country.country_id == country_id))
    if (len(country_data['data']) == 0): ### checking whether country already exists or not (does not exists in this case)
        country_input_data = {}
        country_input_data['country_id'] = country_id
        country_input_data['country_name'] = request.json['country_name']
        add_country(country_input_data) ### adding a new country
        del input_data['country_name']
        add_institution(input_data) ### adding a new institution
        return ("Institution and Country added successfully")
    if (len(country_data['data']) != 0): ### checking whether country already exists or not (exists in this case)
        if request.json['country_name'] == country_data['data'][0]['country_name']: ### checking country_id exists with same name
            del input_data['country_name']
            add_institution(input_data) ### adding a new institution
            return ("Institution added successfully and Country Id already existed")
        else:
            return ("Country Id already exists with different name")

### PUT RestAPI to update country details
@api.route("/countries/<int:country_id>", methods=['PUT'])
def update_country(country_id):
    country_id = request.json['country_id']
    country_data = serialize(db_session.query(Country).filter(Country.country_id == country_id))
    if (len(country_data['data']) != 0): ### checking whether country_id exists or not (exists in this case)
        db_session.query(Country).filter(Country.country_id == country_id).update({Country.country_name:request.json['country_name'],
        Country.inserted_date: datetime.datetime.now().date()}, synchronize_session = False)
        db_session.commit()
        return ("Updated Country Succesfully")
    
    if (len(country_data['data']) == 0): ### checking whether country_id exists or not (does not exists in this case)
        return ("Country Id does not exist")

### PUT RestAPI to update institution details
@api.route("/institutions/<int:institution_id>", methods=['PUT'])
def update_institution(institution_id):
    institution_id = request.json['institution_id']
    institution_data = serialize(db_session.query(Institution).filter(Institution.institution_id == institution_id))
    if (len(institution_data['data']) != 0):  ### checking whether institution_id exists or not (exists in this case)
        db_session.query(Institution).filter(Institution.institution_id == institution_id).update({Institution.institution_name: request.json['institution_name'],
            Institution.city_id: request.json['city_id'],
            Institution.city_name: request.json['city_name'],
            Institution.country_id: request.json['country_id'],
            Institution.course_count: request.json['course_count'],
            Institution.inserted_date: datetime.datetime.now().date()}, synchronize_session = False)
        db_session.commit()
        return ("Updated Institution Succesfully")

    if (len(institution_data['data']) == 0): ### checking whether institution_id exists or not (exists in this case)
        return ("Institution Id does not exist")

### DELETE RestAPI to delete a country
@api.route("/countries/<int:country_id>", methods = ['DELETE'])
def delete_country(country_id):
    country_data = serialize(db_session.query(Country).filter(Country.country_id == country_id))
    if (len(country_data['data']) != 0):  ### checking whether country_id exists or not (exists in this case)
        db_session.query(Country).filter(Country.country_id == country_id).delete()
        db_session.commit()
        return ("Deleted Country Succesfully")
    
    if (len(country_data['data']) == 0):  ### checking whether country_id exists or not (does not exists in this case)
        return ("Country Id does not exist")

### DELETE RestAPI to delete a institution
@api.route("/institutions/<int:institution_id>", methods = ['DELETE'])
def delete_institution(institution_id):  ### checking whether institution_id exists or not (exists in this case)
    institution_data = serialize(db_session.query(Institution).filter(Institution.institution_id == institution_id))
    if (len(institution_data['data']) != 0):
        db_session.query(Institution).filter( Institution.institution_id == institution_id).delete()
        db_session.commit()
        return ("Deleted Institution Succesfully")

    if (len(institution_data['data']) == 0):  ### checking whether institution_id exists or not (exists in this case)
        return ("Institution Id does not exist")