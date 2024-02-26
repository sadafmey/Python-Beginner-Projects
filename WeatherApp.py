import requests


def fetch_weather_data(location):
   
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap.
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit. Because we're all about keeping it metric, unless you're into Fahrenheit for some reason.
    }
    
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    
    return weather_data

def display_weather(weather_data):
    
    if weather_data['cod'] == 200:
        print(f"Weather in {weather_data['name']}:")
        print(f"Description: {weather_data['weather'][0]['description']}")  # Because sometimes, "It's raining cats and dogs" just isn't literal enough.
        print(f"Temperature: {weather_data['main']['temp']}°C")  # Temperature: The most important number in your life right now. Well, until the next update.
        print(f"Humidity: {weather_data['main']['humidity']}%")  # Humidity: Making bad hair days worse since forever.
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")  # Wind Speed: Because we all need a little push in life, don't we?
    else:
        print("City not found. Please enter a valid city name or ZIP code. Or perhaps consider a remote tropical island with no weather data.")
        
def main():
    location = input("Enter city name or ZIP code: ")
    weather_data = fetch_weather_data(location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()