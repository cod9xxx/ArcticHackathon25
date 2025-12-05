import sqlite3
import requests

WEATHER_ICONS = {
    'clear': '☀️Солнечно',
    'partly-cloudy': '⛅Немного облачно',
    'cloudy': '☁️Облачно',
    'overcast': '🌥️Облачно',
    'drizzle': '🌦️Дождливо',
    'light-rain': '🌦️Дождливо',
    'rain': '🌧️Дождь',
    'light-snow': '🌨️Легкий снег',
    'snow': '❄️Снег',
    'storm-slush-snow': '🌨️Буря',
    'hail': '🌨️Град',
    'thunderstorm': '⛈️Гроза',
    'thunderstorm-with-rain': '⛈️Гроза с градом',
    'thunderstorm-with-hail': '⛈️Гроза с дождем',
    'fog': '🌫️Туманно',
    'dust': '🌫️Пустынно',
    'smog': '🌫️Смог',
    'wet-snow': '🌨️Мокрый снег'
}

STATIONS = {
    1: {"name": "McMurdo", "coords": (-77.85, 166.67)},
    2: {"name": "Amundsen-Scott", "coords": (-90.00, 0.00)},
    3: {"name": "Vostok", "coords": (-78.46, 106.84)},
    4: {"name": "Esperanza", "coords": (-63.40, -57.00)},
    5: {"name": "Union Glacier", "coords": (-79.77, -82.91)}
}

YANDEX_API_KEY = "46cd6916-0196-4170-98ae-1f0350d88d67"
BASE_URL = "https://api.weather.yandex.ru/v2/forecast"


def get_weather(station_id):
    try:
        station = STATIONS[station_id]
        lat, lon = station["coords"]

        headers = {"X-Yandex-API-Key": YANDEX_API_KEY}
        params = {
            'lat': lat,
            'lon': lon,
            'lang': 'ru_RU',
            'limit': 1,
            'hours': 'false',
            'days': '1'
        }

        response = requests.get(BASE_URL, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        current = data['forecasts'][0]['parts']['day_short']
        temp = current['temp']
        feels_like = current.get('feels_like', temp)
        wind_speed = current['wind_speed']
        try:
            weather_desc = WEATHER_ICONS[current['condition']]

        except KeyError:
            weather_desc = current['condition']
        pressure = current.get('pressure_mm', '—')
        humidity = current.get('humidity', '—')

        return {
            'name': station['name'],
            'temp': temp,
            'feels_like': feels_like,
            'wind': wind_speed,
            'condition': weather_desc,
            'pressure': pressure,
            'humidity': humidity
        }

    except Exception as e:
        return {'name': STATIONS[station_id]['name'], 'error': str(e)[:50]}


conn = sqlite3.connect('arctic_centres.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS arctic_centres (
        id INTEGER PRIMARY KEY,
        name TEXT,
        condition TEXT,
        temp INTEGER,
        pressure REAL,
        humidity INTEGER,
        feels_like INTEGER
    )
    ''')
conn.commit()

stations = []
for station_id in STATIONS:
    weather = get_weather(station_id)
    if 'error' not in weather:
        stations.append((
            weather['condition'],
            weather['temp'],
            weather['pressure'] if weather['pressure'] != '—' else None,
            weather['humidity'] if weather['humidity'] != '—' else None,
            weather['wind'],
            station_id
        ))
    else:
        print(f"Ошибка для {STATIONS[station_id]['name']}: {weather['error']}")

if stations:
    cursor.executemany('''
            UPDATE arctic_centres 
            SET condition = ?, temp = ?, pressure = ?, humidity = ?, wind = ?
            WHERE id = ?
        ''', stations)
    conn.commit()

conn.close()