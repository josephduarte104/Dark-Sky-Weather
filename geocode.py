import argparse as ag
import requests as req

from urllib.parse import quote

def getLatLonFromAddress(input_address):
    '''
    Function to retreive the lat/lon coordinates from any input address.
    Lat/lon coordinate for the input_address are fetched from the Google Maps API.

    Inputs:
        1.  input_address  ::  kwkw - Fill in docs for input
    Outputs:
        2.  lat, lon  ::  kwkw - Fill in docs for output
    '''
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    encoded_input_address = quote(input_address)
    json_api_address = url + encoded_input_address

    r = req.get(json_api_address)
    lat = r.json()['results'][0]['geometry']['location']['lat']
    lon = r.json()['results'][0]['geometry']['location']['lng']

    # kwkw - index 0 of 'results' accesses an object of objects
    return lat, lon

if __name__ == '__main__':

    parser = ag.ArgumentParser(
        description = 'Fetching lat/lon address from the Google Maps geocode API'
    )
    parser.add_argument(
        '-t',
        action = 'store_true',
        default = False,
        help = '''
        Boolean trigger to test method(s) functionality.
        '''
    )
    parser.add_argument(
        '--input_address',
        action = 'store',
        type = str,
        help = '''
        String object specifying the desired address that the lat/lon xcoordinates are to be fetched for.
        Example: "xxxx Vancouver B.C., Canada"
        '''
    )
    args = parser.parse_args()

    # kwkw - Testing method behaviour
    if args.t:
        print('\nTesting method functionality\n')
        lat, lon = getLatLonFromAddress(args.input_address)
        print('%s:\n\nLat: %f\nLon: %f\n' % (args.input_address, lat, lon))
