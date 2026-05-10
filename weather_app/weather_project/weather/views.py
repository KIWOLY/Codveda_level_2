import os

import requests
from django.contrib import messages
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

API_URL = "https://api.openweathermap.org/data/2.5/weather"


@require_http_methods(["GET", "POST"])
def index(request):
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.POST.get("city", "").strip()
        if not city:
            messages.error(request, "Please enter a city name.")
        else:
            api_key = os.getenv("OPENWEATHER_API_KEY")
            if not api_key:
                error_message = "Missing API key. Set OPENWEATHER_API_KEY in your environment."
            else:
                params = {
                    "q": city,
                    "appid": api_key,
                    "units": "metric",
                }
                try:
                    response = requests.get(API_URL, params=params, timeout=10)
                    data = response.json()

                    if response.status_code != 200:
                        error_message = data.get("message", "City not found. Try again.")
                    else:
                        weather_data = {
                            "city": data.get("name", city),
                            "temperature": data["main"]["temp"],
                            "description": data["weather"][0]["description"].title(),
                            "humidity": data["main"]["humidity"],
                            "wind_speed": data["wind"]["speed"],
                            "icon": data["weather"][0]["icon"],
                        }
                        _store_recent_city(request, city)
                except requests.RequestException:
                    error_message = "Weather service is unavailable. Please try again."

    context = {
        "weather": weather_data,
        "error_message": error_message,
        "recent_searches": request.session.get("recent_cities", []),
    }
    return render(request, "weather/index.html", context)


def _store_recent_city(request, city: str) -> None:
    recent = request.session.get("recent_cities", [])
    if city in recent:
        recent.remove(city)
    recent.insert(0, city)
    request.session["recent_cities"] = recent[:5]
