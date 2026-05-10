# Weather Dashboard (Django)

A beginner-friendly Django web app that fetches real-time weather data from the OpenWeatherMap API. Search any city to see current conditions, temperature, humidity, wind speed, and icon-based visuals.

## Features

- Search by city name
- Real-time weather data (OpenWeatherMap)
- Displays temperature, condition, humidity, wind speed, and icon
- Friendly error messages for invalid cities or API issues
- Recent search history (stored in session)
- Responsive, modern UI

## Tech Stack

- Python
- Django
- requests
- HTML/CSS

## Project Structure

```
manage.py
weather_project/
    settings.py
    urls.py
    wsgi.py
    asgi.py
weather/
    migrations/
    templates/
        weather/
            index.html
    static/
        weather/
            style.css
    views.py
    urls.py
    admin.py
```

## Setup

From the project root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install django requests
```

## Get an API Key

1) Create an account at https://openweathermap.org/
2) Generate an API key from your dashboard.
3) Export the key in your terminal:

```bash
export OPENWEATHER_API_KEY="your_key_here"
```

Note: New keys may take 10–60 minutes to activate.

## Run the App

```bash
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

## API Details Used

- Endpoint: `https://api.openweathermap.org/data/2.5/weather`
- Query params: `q` (city), `appid` (API key), `units=metric`
- Fields displayed:
  - `name`
  - `main.temp`
  - `weather[0].description`
  - `main.humidity`
  - `wind.speed`
  - `weather[0].icon`

## Troubleshooting

- If you see “Invalid API key”, confirm the key works with:
  ```bash
  curl "https://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid=$OPENWEATHER_API_KEY"
  ```
- If it still fails, your key might not be activated yet.

## Optional Enhancements

- Dark mode
- 5-day forecast
- Geolocation-based weather
- AJAX search
