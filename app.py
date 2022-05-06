from flask import Flask, render_template
from settings import CONTINENTS
from utils import get_all_countries_from_continent, get_iso_from_country, get_random_country_from_continent

from random import shuffle

app = Flask(__name__)

@app.route('/')
def home():
    images = dict()
    for continent in CONTINENTS:
        images[continent] = f'/static/maps/{continent}/{continent}.png'

    return render_template('index.html', images=images)


@app.route('/<continent>/index')
def countries_index(continent):
    countries = get_all_countries_from_continent(continent)
    for country in countries:
        country['image_url'] = f'/static/maps/{continent}/{country["iso"]}/256.png'.replace(' ', '%20')
    
    return render_template('countries_index.html', countries=countries, continent=continent)

@app.route('/<continent>/quiz')
def quiz(continent):
    continent = continent.replace('%20', ' ')
    country = get_random_country_from_continent(continent)
    country_name = country['country']
    country_iso = country['iso']
    territory_image_file = '256.png'
    territory_image_url = f'/static/maps/{continent}/{country_iso}/{territory_image_file}'.replace(' ', '%20')

    answers = [country_name]
    for _ in range(3):
        # print('inside for')
        # print(continent)
        
        answer = get_random_country_from_continent(continent)['country']
        while answer in answers:
            answer = get_random_country_from_continent(continent)['country']
        
        answers.append(answer)

    territory = {
        "country": country_name,
        "image_url": territory_image_url
    }
    
    return render_template('quiz.html', country=territory, continent=continent, answers=answers)

