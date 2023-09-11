import requests

def get_weather(city):
    api_key = 'YOUR_API_KEY'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    complete_url = f'{base_url}q={city}&appid={api_key}&units=metric'
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main_data = data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        weather_info = data["weather"][0]["description"]
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Weather: {weather_info}')
    else:
        print("City not found")

city = input("Enter a city: ")
get_weather(city)
