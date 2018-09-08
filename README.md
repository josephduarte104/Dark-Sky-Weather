# Dark Sky Weather
![](https://github.com/kdubss/Dark-Sky-Weather/blob/master/static/img/landing-page.png)
---
Web-app that fetches hourly and daily *forecast* (and *hindcast*) weather data from
the [Dark Sky API](forecast.io).

##  Installing / Getting Started
---

### Setting up Dev
Clone the project and install the dependencies
  > ```git clone https://github.com/kdubss/Dark-Sky-Weather your-project-name```
  > ```cd your-project-name```

If running Python3,
  > ```pip3 install -r requirements.txt```

Elsif Python2,
  > ```pip install -r requirements.txt```
  
Once all the dependencies have been successfully installed, enter the following in the terminal to start the server
  > ```python3 app.py```
  
### Dark Sky API-key
Before anything, make sure to register with [Dark Sky](https://darksky.net/dev/register) to get access to your ```api key```.
Once you have your key, it's a good idea to place it within ```local_settings.py``` file which is will not be version controlled (*via.* ```.gitignore```).

### Geocode Location
Currently, the address location in ```app.py``` is hardcoded to Vancouver B.C., Canada, so make sure to change this.
(__Note:__ This will be changed as the app is developed to get a user-specified location from the browser).


These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
*See the deployment for notes on how to deploy the project on a live system*.

### Prerequisites
WIP

## Running Tests
---
WIP

## Deployment
---
WIP

## Built With
---
  - Flask - Found [here](http://flask.pocoo.org/)
  - Python3 - [Windows](https://www.python.org/downloads/windows/) or [MacOS](https://www.python.org/downloads/)

## Contributing
---
WIP

## Versioning
---
WIP

## Authors
---
Kang Wang

## License
---
This project is licensed under the MIT license - See the [License.md](https://github.com/angular/angular.js/blob/master/LICENSE) for details

## Acknowledgements
---
  - Bootstrap styling and *some* images downloaded from [Start Bootstrap](https://startbootstrap.com/template-overviews/grayscale/)