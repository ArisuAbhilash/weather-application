from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)
API_KEY = '18df78adeef92fe44cea948b865ab59e'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    forecast = []

    if request.method == 'POST':
        city = request.form['city']
    else:
        city = "Delhi"

    # Get coordinates
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    geo_response = requests.get(geo_url).json()

    if geo_response:
        lat = geo_response[0]['lat']
        lon = geo_response[0]['lon']

        # Current weather
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        weather_data = requests.get(weather_url).json()

        # 5-day forecast
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        forecast_data = requests.get(forecast_url).json()

        # Create current weather dictionary
        if weather_data.get('cod') == 200:
            weather = {
                'city': weather_data['name'],
                'temp': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'].title(),
                'humidity': weather_data['main']['humidity'],
                'wind': weather_data['wind']['speed'],
                'precip': weather_data['clouds']['all'],
                'time': datetime.now().strftime("%A %H : %M")
            }

        # 5-day forecast (pick one forecast per day at 12:00)
        used_days = set()
        for entry in forecast_data['list']:
            date_txt = entry['dt_txt']
            day = datetime.strptime(date_txt, '%Y-%m-%d %H:%M:%S').strftime('%a')

            if '12:00:00' in date_txt and day not in used_days:
                forecast.append({
                    'day': day,
                    'temp_min': int(entry['main']['temp_min']),
                    'temp_max': int(entry['main']['temp_max']),
                    'icon': f"http://openweathermap.org/img/wn/{entry['weather'][0]['icon']}@2x.png"
                })
                used_days.add(day)

                if len(forecast) == 5:
                    break

    return render_template('index.html', weather=weather, forecast=forecast)

if __name__ == '__main__':
    app.run(debug=True)
