
import requests

def get_weather(api_key, city):
    '''Fetch the current weather information for a specified city using the OpenWeatherMap API.'''
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return None

if __name__ == "__main__":
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter the city name: ")
    weather = get_weather(api_key, city)
    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Could not fetch weather information. Please check the city name or API key.")
