import sys
import requests
import time
import os

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
    'smog': '🌫️Смог'
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


def clear_screen():
    """Очистка консоли"""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_weather(station_id):
    """Получить погоду для конкретной станции"""
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
        weather_desc = WEATHER_ICONS[current['condition']]
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


def print_weather(station_id, weather_data):
    """Красиво вывести погоду станции"""
    station = STATIONS[station_id]
    clear_screen()

    print("🌍" + "=" * 50 + "🌍")
    print(f"     Погода на станции {station['name']}")
    print("=" * 50 + "🌍")
    print()

    if 'error' in weather_data:
        print(f"❌ Ошибка: {weather_data['error']}")
    else:
        print(f"🌡️  Температура:      {weather_data['temp']}°C")
        print(f"😓  Ощущается как:    {weather_data['feels_like']}°C")
        print(f"💨  Ветер:            {weather_data['wind']} м/с")
        print(f"☁️   Условия:          {weather_data['condition']}")
        print(f"📊  Давление:         {weather_data['pressure']} мм рт.ст.")
        print(f"💧  Влажность:        {weather_data['humidity']}%")

    print()
    print("🌍" + "=" * 50 + "🌍")
    print("Нажмите Enter для обновления...")


def print_all_stations():
    """Вывести погоду всех станций"""
    clear_screen()
    print("🌍" + "=" * 70 + "🌍")
    print("     Погода на всех антарктических станциях")
    print("=" * 70 + "🌍")
    print()

    all_weather = {}
    for station_id in STATIONS:
        print(f"📍 {STATIONS[station_id]['name']}: ", end="")
        weather = get_weather(station_id)
        all_weather[station_id] = weather

        if 'error' not in weather:
            print(f"{weather['temp']}°C, {weather['condition'][:30]}...")
        else:
            print("Ошибка загрузки")

    print()
    print("🌍" + "=" * 70 + "🌍")
    print("Введите номер станции (1-5) или 0 для выхода")
    return all_weather


def main():
    while True:
        clear_screen()
        print("🌍 АНТАРКТИЧЕСКИЕ СТАНЦИИ 🌍")
        print("=" * 40)
        print("1 - McMurdo")
        print("2 - Amundsen-Scott")
        print("3 - Vostok")
        print("4 - Esperanza")
        print("5 - Union Glacier")
        print("6 - Все станции")
        print("0 - Выход")
        print("=" * 40)

        try:
            choice = input("\nВыберите станцию (0-6): ").strip()
            choice = int(choice)

            if choice == 0:
                print("До свидания! 👋")
                break
            elif choice == 6:
                print_all_stations()
                input("\nНажмите Enter...")
            elif 1 <= choice <= 5:
                weather = get_weather(choice)
                print_weather(choice, weather)
                input()
            else:
                print("❌ Неверный выбор! Введите 0-6")
                time.sleep(1)

        except ValueError:
            print("❌ Введите цифру!")
            time.sleep(1)
        except KeyboardInterrupt:
            print("\n\nДо свидания! 👋")
            break


if __name__ == "__main__":
    print("🔄 Загрузка... Не забудьте указать YANDEX_API_KEY!")
    main()
