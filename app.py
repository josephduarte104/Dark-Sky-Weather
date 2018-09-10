'''
Python-Flask API to fetch, parse, and visualize weather data from the Dark Sky API (forecast.io)
'''
import darksky_api_request as api
import darksky_api_methods as dsky

from flask import Flask, jsonify, render_template, url_for, redirect
from flask_mako import MakoTemplates
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View

app = Flask(__name__)
nav = Nav(app)

# kwkw - Build navbar
topbar = Navbar('', 
                View('Home', 'index'), 
                View('About', 'about_page'),
                View('Contact', 'contact_page')
                )

nav.register_element('top', topbar)
nav.init_app(app)

# > Redirected endpoints
@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def redirect_to_root():
    return redirect('/darkskyweather/api/v1.0/', code = 302)

@app.route('/about', methods = ['GET'])
def redirect_to_about():
    return redirect('/darkskyweather/api/v1.0/about', code = 302)

# 1. Landing Page/Index Page:
@app.route('/darkskyweather/api/v1.0/', methods = ['GET'])
def index():
    return render_template('index.html')
    
# 2. About Page
@app.route('/darkskyweather/api/v1.0/about', methods = ['GET'])
def about_page():
    return render_template('about.html', title = 'About')





# > Weather Data:
@app.route('/alerts', methods = ['GET'])
def redirect_to_alerts():
    return redirect('/darkskyweather/api/v1.0/forecast/alerts/')

@app.route('/forecast', methods = ['GET'])
def redirect_to_forecast():
    return redirect('/darkskyweather/api/v1.0/forecast/', code = 302)

@app.route('/darkskyweather/api/v1.0/forecast/', methods = ['GET'])
@app.route('/darkskyweather/api/v1.0/forecast/index', methods = ['GET'])
def get_index():
    forecast = api.getForecastDataFromDarkSky('Vancouver Canada')
    # kwkw - returns a python dict
    data = forecast.json()
    return jsonify(data)

@app.route('/darkskyweather/api/v1.0/forecast/alerts/', methods = ['GET'])
def get_forecast_alerts():
    # kwkw - Need to format string output
    alert = dsky.getForecastWeatherAlerts('Vancouver Canada')
    return alert

@app.route('/darkskyweather/api/v1.0/forecast/daily/', methods = ['GET'])
def get_daily_data():
    # kwkw - WIP - will have to refactor once full MVP is constructed.
    forecast_response = api.getForecastDataFromDarkSky('Vancouver Canada')
    daily_forecast = dsky.getDailyForecastData(forecast_response.json())
    return jsonify(daily_forecast)

@app.route('/darkskyweather/api/v1.0/forecast/hourly/', methods = ['GET'])
def get_hourly_data():
    # kwkw - WIP - will have to refadtor once MVP website is built up.
    forecast_response = api.getForecastDataFromDarkSky('Vancouver Canada')
    # kwkw - WIP - hourly data returns an array of
    hourly_forecast = dsky.getHourlyForecastData(forecast_response.json())
    return jsonify(hourly_forecast)

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
