'''
Python-Flask API to fetch, parse, and visualize weather data from the Dark Sky API (forecast.io)
'''
import darksky_api_request as api

from flask import Flask, jsonify, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def get_index():
    forecast = api.getForecastDataFromDarkSky('Vancouver Canada')
    data = forecast.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
