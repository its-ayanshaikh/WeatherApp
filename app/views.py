from django.shortcuts import render
import requests
from django.conf import settings
from datetime import datetime

# Create your views here.
def get_weather_data(city):
    api_key = settings.WEATHER_API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # use "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    return response.json()

def home(request):
    city = request.GET.get("city", "Ahmedabad")  # Default city if none is specified
    weather_data = get_weather_data(city)
    current_datetime = datetime.now().strftime("%A, %B %d, %Y at %I:%M %p")
    
    context = {
        "city_name": city,
        "datetime": current_datetime,
        "weather_description": weather_data.get("weather", [{}])[0].get("description", "N/A"),
        "weather_icon": weather_data.get("weather", [{}])[0].get("icon", "01d"),
        "temperature": weather_data.get("main", {}).get("temp"),
        "temp_min": weather_data.get("main", {}).get("temp_min"),
        "temp_max": weather_data.get("main", {}).get("temp_max"),
        "real_feel": weather_data.get("main", {}).get("feels_like"),
        "humidity": weather_data.get("main", {}).get("humidity"),
        "wind_speed": weather_data.get("wind", {}).get("speed"),
        "pressure": weather_data.get("main", {}).get("pressure"),
    }
    temp_min = weather_data.get("main", {}).get("temp_min"),
    temp_max = weather_data.get("main", {}).get("temp_max"),
    print(temp_min, temp_max)
    return render(request, 'index.html', context) 

