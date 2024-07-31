import requests

def get_weather(api_key, city):
    try:
        base_url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        
        data = response.json()
        
        if data['cod'] == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            print(f"Weather in {city}: {weather_description}")
            print(f"Temperature: {temperature}°C")
        else:
            print(f"Error: {data['message']}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")

if __name__ == "__main__":
    api_key = "afe72a4da5b0392c920e53f98a0b7907"  # Replace with your actual API key
    city = input("Enter the city name: ")
    get_weather(api_key, city)
