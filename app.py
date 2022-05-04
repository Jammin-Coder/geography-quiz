from django.shortcuts import render
from flask import Flask, render_template
from iso_utils import get_country_name_by_iso, get_iso_name, get_random_territory_from_region
from utils import get_continents

app = Flask(__name__)

@app.route('/')
def home():
    continents = get_continents()
    images = dict()
    for continent in continents:
        images[continent] = f'/static/maps/{continent}/{continent}.png'

    return render_template('index.html', images=images)

@app.route('/<continent>/quiz')
def quiz(continent):
    territory_name = get_random_territory_from_region(continent)
    territory_iso = get_iso_name(territory_name)
    territory_image_file = '256.png'
    territory_image_url = f'/static/maps/{continent}/{territory_iso}/{territory_image_file}'.replace(' ', '%20')

    territory = {
        "name": territory_name,
        "image_url": territory_image_url
    }
    return render_template('quiz.html', territory=territory, continent=continent)

