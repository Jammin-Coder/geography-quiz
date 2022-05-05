import json
import random
import os
from database import db_connect
from settings import CONTINENTS_TABLE_NAME

def read(path):
    with open(path, 'r') as f:
        return f.read()


def write(path, contents):
    with open(path, 'w') as f:
        f.write(contents)

def get_iso_from_country_by_continent(target_country, continent_name):
    db = db_connect()
    cursor = db.cursor()
    cursor.execute(
        'SELECT * FROM continents WHERE continent_name = %(continent_name)s;',
        {
            'continent_name': continent_name
        }
    )
    countries_row = cursor.fetchone()
    db.close()

    countries_list = json.loads(countries_row[1])['countries']
    for country_object in countries_list:
        if country_object['country'] == target_country:
            return country_object['iso']

    return None


def get_iso_from_country(target_country):
    db = db_connect()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM continents;')
    continents = cursor.fetchall()
    db.close()

    for continent in continents:
        countries = json.loads(continent[1])['countries']
        for country in countries:
            if country['country'] == target_country:
                return country['iso']
            
    return None


def get_country_name_by_iso(target_iso):
    pass


def get_random_territory_from_region(region):
    pass



