# Weather App

This is a simple Python script to fetch and display the current weather for a specified city using the OpenWeatherMap API.

## Description

The script takes a city name as input and retrieves the current weather information, including the weather description and temperature in Celsius. It handles various exceptions that may occur during the API request.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository to your local machine:
```bash
    git clone https://github.com/yourusername/weather-app.git
```
2. Navigate to the project directory:
```bash
    cd weather-app
```
3. Install the required Python modules:
```bash
    pip install requests
```

## Usage

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).
2. Open the `weather_app.py` file and replace the placeholder API key (`afe72a4da5b0392c920e53f98a0b7907`) with your actual API key.
3. Run the script:
```bash
    python weather_app.py
```
4. Enter the city name when prompted to get the weather information.

## Example

```bash
$ python weather_app.py
Enter the city name: London
Weather in London: clear sky
Temperature: 15°C
```