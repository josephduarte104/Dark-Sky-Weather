'''
Various functions/methods for I/O and data parsing & manipulation methods for weather data fetched from the Dark Sky API (api.darksky.net).
'''
import argparse as ag
import pandas as pd
import datetime as dt
import os
import darksky_api_request as api
import geocode as geo

from flask import jsonify

def getForecastResponseFromRequest():
    '''
    Method of sending a request to the Dark Sky API, then handling the response by calling on the .json() method to convert the response to a Python Dict object.

    Output:
        1.  data_dict  ::  Python dict object containing key-value pairs for hourly data fetched from api.darksky.net
    '''
    data_dict = api.getForecastDataFromDarkSky('Vancouver Canada')
    data_dict = data_dict.json()

    return data_dict

def getForecastWeatherAlerts(address):
    '''
    Method to fetch forecasted weather alerts.
    This method will accept the a Python dict as Input and print out the alerts as a string.

    Input:
        1.  address  ::  Python Str object specifying the address for where forecast weather alerts is to be fetched for.
    Output:
        2.  Alert Msg  ::  A string object outputing the alerts from the alerts attribute (which is an array of objects - with following attributes:
            - description (string)
            - expires (unix time stamp)
            - regions affected (array)
            - severity (string)
            - time of alert (unix time stamp)
            - title (string)
            - uri (string)
    '''
    darksky_response = api.getForecastDataFromDarkSky(address)
    json_data_dict = darksky_response.json()
    weather_alerts_content = json_data_dict['alerts'][1]
    weather_alert_out = \
'''
***  %s  ***

%s

Regions Affected:
%s

Severity:
%s

Time:
%s

''' % (
    weather_alerts_content['title'],
    weather_alerts_content['description'],
    weather_alerts_content['regions'],
    weather_alerts_content['severity'],
    api.getHumanReadableTimeFromUnixTimeStamp(weather_alerts_content['time'])
)

    return weather_alert_out

def getDailyForecastData(json_dict):
    '''
    Method to parse the daily data from the Python dictionary object returned from the request to the Dark Sky API.
    Daily data responses from api.darksky.net will return an array of weather objects for 8 days.

    Input:
        1.  data_dict  ::  Python dict object containing key-value pairs for the daily data parsed from the JSON response from api.darksky.net.
    Output:
        2.  daily_data  ::  Python dict object containing the daily data parsed from the JSON response from api.darksky.net.
    '''
    daily_data = json_dict['daily']['data']

    # kwkw - Returns an array of data objects
    return daily_data

def getHourlyForecastData(json_dict):
    '''
    Method to parse the hourly data from the Python dictionary objec returned from the request to the Dark Sky API.

    Input:
        1.  json_dict  ::  Python dict object containing key-value pairs for the hourly data parsed from the JSON response from api.darksky.net.
    Output:
        2.  hourly_data  ::  Python dict object containing the daily data parsed from the JSON response from api.darksky.net.
    '''
    hrly_data = json_dict['hourly']['data']

    # kwkw - Returns an array of data objects(?):
    return hrly_data

def getCelsiusFromFahrenheit(temp_f):
    '''
    '''
    pass

def getFahrenheitFromCelsius(temp_c):
    '''
    '''
    pass


if __name__ == '__main__':

    prsr = ag.ArgumentParser(
        description = 'Suite of CLI commands to test method behaviour and functionality.'
    )
    prsr.add_argument(
        '-t',
        action = 'store_true',
        default = False,
        help = 'Boolean trigger to test module method functionality and behaviour.'
    )
    prsr.add_argument(
        '--input_address',
        action = 'store',
        type = str,
        help = '''
        String object specifying the desired address that the lat/lon xcoordinates are to be fetched for.
        Example: "xxxx Vancouver B.C., Canada"
        '''
    )
    prsr.add_argument(
        '--daily',
        action = 'store_true',
        default = False,
        help = 'Boolean arg to trigger the testing of fetching daily data from api.darksky.net.'
    )
    prsr.add_argument(
        '--hourly',
        action = 'store_true',
        default = False,
        help = 'Boolean arg to trigger the testing of fetching hourly data from api.darksky.net.'
    )
    args = prsr.parse_args()

    if args.t:
        if args.input_address:
            if args.daily:
                darksky_response = getForecastResponseFromRequest()
                daily_data = getDailyForecastData(darksky_response)
                print(len(daily_data))
            elif args.hourly:
                darksky_response = getForecastResponseFromRequest()
                hrly_data = getHourlyForecastData(darksky_response)
                print(len(hourly_data))
