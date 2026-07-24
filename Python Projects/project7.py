import requests

API_KEY = 'b64a712362b30f00d2a7cf8f90d6f73f'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter city name: ")

# Complete URL
url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200 and "main" in data:
    main = data["main"]
    weather = data["weather"][0]
    print(f"\nWeather in {city.upper()}:\n")
    print(f"🌡 Temperature: {main['temp']}°C")
    print(f"🤒 Feels Like: {main['feels_like']}°C")
    print(f"💧 Humidity: {main['humidity']}%")
    print(f"☁️ Description: {weather['description'].capitalize()}")
else:
    print("❌ Error: ", data.get("message", "Something went wrong."))