from itertools import count
import json
import random
from database import db_connect
from settings import CONTINENTS, CONTINENTS_TABLE_NAME

def read(path):
    with open(path, 'r') as f:
        return f.read()


def write(path, contents):
    with open(path, 'w') as f:
        f.write(contents)

def get_iso_from_country_by_continent(target_country, continent_name):
    """
    Selects a continent from the database, loops over its countries looking for the provided
    'target_country'. When it's found, it returns it's ISO value.
    """
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
    """
    Selects all of the continents, loops over their countries to look for
    'target_country'. A country that matches 'target_country' is found,
    return the matched country's ISO value.
    """
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


def get_country_name_from_iso_by_continent(target_iso, continent_name):
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
        if country_object['iso'] == target_iso:
            return country_object['country']

    return None

def get_country_name_from_iso(target_iso):
    db = db_connect()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM continents;')
    continents = cursor.fetchall()
    db.close()

    for continent in continents:
        countries = json.loads(continent[1])['countries']
        for country in countries:
            if country['iso'] == target_iso:
                return country['country']
            
    return None


def get_random_country():
    db = db_connect()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM continents;')
    continents = cursor.fetchall()
    db.close()

    cont_index = random.randrange(0, len(CONTINENTS))
    countries = json.loads(continents[cont_index][1])["countries"]
    rand_country_index = random.randrange(0, len(countries))
    country = countries[rand_country_index]
    return country


def get_random_country_from_continent(continent_name):
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
    
    countries = json.loads(countries_row[1])['countries']
    rand_index = random.randrange(0, len(countries))
    country = countries[rand_index]
    return country



