<h1 align="center">
   <a href="#"> Flask Weather API </a>
</h1>

<h3 align="center">
    A simple API that gives information about the weather in a specified location.
</h3>

<h4 align="center"> 
	 Status: In progress
</h4>

<p align="center">
 <a href="#about">About</a> •
 <a href="#routes">Routes</a> • 
 <a href="#how-it-works">How it works</a> • 
 <a href="#tech-stack">Tech Stack</a> • 
 <a href="#author">Author</a> •
</p>

## About

This API serves information about a specified location and in a specified language, defaulting to english. It uses a web scraper to search for the weather information based on the parameters entered by the client. The web scraper will search and retrieve the information from the web and give it back to the client in object format.

---

## Routes

```yml
    GET /weather
    - Route to get weather data from location
    - Query parameters:
        - location: any location by name (required)
        - lang: ISO 639-1 language codes (optional), defaults to 'EN'
    - Response example:
        {
            "message": "success",
            "data": {
                "celsius": "26",
                "fahrenheit": "78",
                "humidity": "86%",
                "location": "Aracati, CE",
                "rain": "3%",
                "speed_km": "14 km/h",
                "speed_mi": "9 mph",
                "weather_type": "Partially cloudy"
            }
        }
```

---

## How it works.

### Pre-requisites

Before you begin, you will need to have [Python](https://www.python.org/) and [chromedriver](https://chromedriver.chromium.org/downloads) installed on your machine.

#### Running the server

```bash

# Clone this repository
$ git clone https://github.com/nogueirayure001/flask-weather-api.git

# Access the project folder in your terminal
$ cd flask-weather-api

# Make a virtual enviroment
$ python3 -m venv venv

# Activate the virtual enviroment
$ . venv/bin/activate

# Set the environment variables on .env
# BASE_URL should be https://www.google.com
# DRIVER_URL should be the path to the chromedriver

# Install the dependencies
$ pip install -r requirements.txt

# Run the application in development mode
$ flask run

# The application will open on the port: 5000 - go to http://localhost:5000

```

---

## Tech Stack

The following tools were used in the construction of the project:

- **[Flask](https://flask.palletsprojects.com/)**
- **[BeautifulSoup](https://beautiful-soup-4.readthedocs.io/)**
- **[Selenium](https://selenium-python.readthedocs.io/)**
- **[Python dotenv](https://github.com/theskumar/python-dotenv)**

---

## Author

[Linkedin](https://www.linkedin.com/in/nogueirayure/)
[Gmail](mailto:nogueirayure1993@gmail.com)
