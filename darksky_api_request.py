'''
API rquests routines from the Dark Sky API (forecast.io)
'''
import requests as req
import time
import argparse as ag

from dateutil import parser
from time import mktime
from local_settings import env
from geocode import getLatLonFromAddress

def getHumanReadableTimeFromUnixTimeStamp(unix_time_stamp):
    '''
    Method to get a human readable time from a unix time stamp.

    Input:
        1.  unix_time_stamp  ::  kwkw - fill out arg docs
    Output:
        2.  pretty_time  ::  Human readable time converted from a unix time stamp.
    '''
    pretty_time = time.strftime(
        '%Y-%m-%d-%H:%M:%S',
        time.localtime(unix_time_stamp)
    )

    return pretty_time

def getUnixTimeStampFromHumanReadableTime(human_readable_time):
    '''
    Method to get the Unix Time Stamp from a human readable time input.
    The function uses the datetime module and the mktime() function which uses the struct_time (9-tuple) to express the time in local time.  The method returns a floating point number.

        1.  human_readable_time  ::  A Human readable time (e.g. '2018-04-02' or 'April 2, 2018')
    Output:
        2.  unix_time_stamp  ::  Unix time stamp converted from a human readable time.
    '''
    time = parser.parse(human_readable_time)
    unix_time_stamp = mktime(time.timetuple())

    return unix_time_stamp

def getForecastDataFromDarkSky(input_address):
    '''
    Forecast request to  https://api.darksky.net/forecast/[api-key]/[lat],[lon] to fetch forecast weather data for the input address.

    Input:
        1.  input_address  ::  Str object specifying the address for where the forecast data is to be fetched for.
    Output:
        2.  r  ::  Respone output object (request.models.Response) from the Dark Sky API request.  The Response object has a .json() method, which will return a Python Dict object of key-value pairs, of forecast weather data parameters.

        Dictionary keys include:
            - alerts
            - daily: daily forecast data
            - hourly: hourly forecast data
            - flags
            - longitude
            - latitude
            - timezone
            - minutely: minute forecast data
            - currently: the current conditions
    '''
    lat, lon = getLatLonFromAddress(input_address)
    url = 'https://api.darksky.net/forecast/%s/%s,%s' % (env['api_key'], str(lat), str(lon))
    r = req.get(url)

    return r

def getTimeMachineDataFromDarkSky(input_address, readable_time):
    '''
    Time-Machine request to the time-machine-url - https://api.darksky.net/forecast/[api-key]/[lat],[lon],[time] to fetch historical weather data from the Dark Sky API.

    Input:
        1.  input_address  ::  Str object specifying the address for where the time-machine (hindcast) data is to be fetched for.
        2.  unix_time_stamp
    Output:
        3.  r  ::  Respone output object (request.models.Response) from the Dark Sky API request.  The Response object has a .json() method, which will return a Python Dict object of key-value pairs, of forecast weather data parameters.

        Python Dictionary Keys:
            - kwkw - Add keys into docs
    '''
    unix_time_stamp = getUnixTimeStampFromHumanReadableTime(readable_time)
    lat, lon = getLatLonFromAddress(input_address)
    url = 'https://api.darksky.net/forecast/%s/%s,%s,%i' % (env['api_key'], str(lat), str(lon), int(unix_time_stamp))
    r = req.get(url)

    return r

if __name__ == '__main__':

    prsr = ag.ArgumentParser(
        description = 'Testing method functionality and behaviour'
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
    args = prsr.parse_args()

    if args.t:
        r = getForecastDataFromDarkSky(args.input_address)
        print(r.json().keys())
        # print(r.json().keys(), '\n\n')
        # r2 = getTimeMachineDataFromDarkSky(args.input_address)
        # print(getHumanReadableTimeFromUnixTimeStamp(3034549485045))
        # print(getUnixTimeStampFromHumanReadableTime('August 21, 2018'))
        # print(getTimeMachineDataFromDarkSky(args.input_address, 'August 18, 2018'))
