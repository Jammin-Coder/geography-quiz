from flask import Flask, render_template
from settings import CONTINENTS
from utils import get_iso_from_country, get_random_country_from_continent

app = Flask(__name__)

@app.route('/')
def home():
    images = dict()
    for continent in CONTINENTS:
        images[continent] = f'/static/maps/{continent}/{continent}.png'

    return render_template('index.html', images=images)

@app.route('/<continent>/quiz')
def quiz(continent):
    country = get_random_country_from_continent(continent)
    country_name = country['country']
    country_iso = country['iso']
    territory_image_file = '256.png'
    territory_image_url = f'/static/maps/{continent}/{country_iso}/{territory_image_file}'.replace(' ', '%20')

    territory = {
        "name": country_name,
        "image_url": territory_image_url
    }
    
    return render_template('quiz.html', territory=territory, continent=continent)

