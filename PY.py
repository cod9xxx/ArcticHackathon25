import sys
import sqlite3

import requests
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow, QCheckBox, QDialog, \
    QButtonGroup
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QSize, Qt
from gigachat import GigaChat

from template_interface_quiz import template_quiz
from template_interface_quiz_score import template_quiz_scores
from template_interface_station import template_station
from template_interface_nature import template_nature
from template_interface_main import template_main
from template_interface_ways import template_ways
from template_interface_facts import template_fact
import io
from PyQt6 import uic


class Encyclopedia(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template_main)
        uic.loadUi(f, self)

        self.setWindowTitle("Интерактивная карта Антарктики")
        self.btn_style_animal()
        self.btn_style_plant()
        self.btn_style_station()
        pixmap = QPixmap('map.png')
        scaled_pixmap = pixmap.scaled(self.mapPhoto_label.size(),
                                      Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        self.mapPhoto_label.setPixmap(scaled_pixmap)
        self.ways_btn.clicked.connect(self.ways)
        pixmap = QPixmap('way_red.png')
        scaled_pixmap = pixmap.scaled(self.way1Photo_label.size(),
                                      Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        self.way1Photo_label.setPixmap(scaled_pixmap)
        self.way1Photo_label.hide()
        pixmap = QPixmap('way_yellow.png')
        scaled_pixmap = pixmap.scaled(self.way2Photo_label.size(),
                                      Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        self.way2Photo_label.setPixmap(scaled_pixmap)
        self.way2Photo_label.hide()

        self.facts_btn.clicked.connect(self.facts)

        self.quiz_btn.clicked.connect(self.quiz)

    def quiz(self):
        self.quiz_window = QuizWindow()
        self.quiz_window.show()

    def facts(self):
        self.fakt_window = Fakt()
        self.fakt_window.show()

    def on_changed(self, index):
        if index == 0:  # Выбрана черточка "-"
            self.way1Photo_label.hide()
            self.way2Photo_label.hide()
        elif index == 1:  # Выбран "Маршрут Джеймса Кука"
            self.way1Photo_label.show()  # Показываем первый маршрут
            self.way2Photo_label.hide()  # Скрываем второй
        elif index == 2:  # Выбран "Маршрут Беллинсгаузна и Лазарева"
            self.way1Photo_label.hide()  # Скрываем первый
            self.way2Photo_label.show()

    def ways(self):
        try:
            dialog = Way()
            if dialog.exec():
                selected_index = dialog.result
                self.on_changed(selected_index)
        except Exception as e:
            print(f"Ошибка восстановления: {e}")

    def btn_style_animal(self):
        self.animal1.setStyleSheet("""QPushButton {
                background-color: transparent;
                border: none;}""")
        pixmap = QPixmap('олень.png')
        scaled_pixmap = pixmap.scaled(QSize(60, 60), Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(scaled_pixmap)
        self.animal1.setIcon(icon)
        self.animal1.setIconSize(QSize(140, 140))
        self.animal1.setProperty("animal_name", "Олень северный")
        self.animal1.clicked.connect(self.btn)

        self.animal2.setStyleSheet("""QPushButton {
                background-color: transparent;
                border: none;}""")
        pixmap = QPixmap('бык.png')
        scaled_pixmap = pixmap.scaled(QSize(60, 60),Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(scaled_pixmap)
        self.animal2.setIcon(icon)
        self.animal2.setIconSize(QSize(140, 140))
        self.animal2.setProperty("animal_name", "Мускусный бык")
        self.animal2.clicked.connect(self.btn)

        self.animal3.setStyleSheet("""QPushButton {
                background-color: transparent;
                border: none;}""")
        pixmap = QPixmap('пингвин.png')
        scaled_pixmap = pixmap.scaled(QSize(60, 60),Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(scaled_pixmap)
        self.animal3.setIcon(icon)
        self.animal3.setIconSize(QSize(140, 140))
        self.animal3.setProperty("animal_name", "Пингвин")
        self.animal3.clicked.connect(self.btn)

        self.animal4.setStyleSheet("""QPushButton {
                background-color: transparent;
                border: none;}""")
        pixmap = QPixmap('морж.png')
        scaled_pixmap = pixmap.scaled(QSize(60, 60),Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(scaled_pixmap)
        self.animal4.setIcon(icon)
        self.animal4.setIconSize(QSize(140, 140))
        self.animal4.setProperty("animal_name", "Морж")
        self.animal4.clicked.connect(self.btn)

        self.animal5.setStyleSheet("""QPushButton {
                background-color: transparent;
                border: none;}""")
        pixmap = QPixmap('песец.png')
        scaled_pixmap = pixmap.scaled(QSize(60, 60),Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(scaled_pixmap)
        self.animal5.setIcon(icon)
        self.animal5.setIconSize(QSize(140, 140))
        self.animal5.setProperty("animal_name", "Песец")
        self.animal5.clicked.connect(self.btn)

    def btn_style_plant(self):
        self.plant1.setStyleSheet("""QPushButton {
                background-color: transparent;
                border: none;}""")
        pixmap = QPixmap('волосовидная.png')
        scaled_pixmap = pixmap.scaled(QSize(60, 60),Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(scaled_pixmap)
        self.plant1.setIcon(icon)
        self.plant1.setIconSize(QSize(140, 140))
        self.plant1.setProperty("animal_name", "Антарктическая волосовидная трава")
        self.plant1.clicked.connect(self.btn)

        self.plant2.setStyleSheet("""QPushButton {
                background-color: transparent;
                border: none;}""")
        pixmap = QPixmap('жемчужина.png')
        scaled_pixmap = pixmap.scaled(QSize(60, 60),Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(scaled_pixmap)
        self.plant2.setIcon(icon)
        self.plant2.setIconSize(QSize(140, 140))
        self.plant2.setProperty("animal_name", "Антарктическая жемчужница")
        self.plant2.clicked.connect(self.btn)

        self.plant3.setStyleSheet("""QPushButton {
                background-color: transparent;
                border: none;}""")
        pixmap = QPixmap('лишайник.png')
        scaled_pixmap = pixmap.scaled(QSize(60, 60),Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(scaled_pixmap)
        self.plant3.setIcon(icon)
        self.plant3.setIconSize(QSize(140, 140))
        self.plant3.setProperty("animal_name", "Антарктический лишайник")
        self.plant3.clicked.connect(self.btn)

        self.plant4.setStyleSheet("""QPushButton {
                background-color: transparent;
                border: none;}""")
        pixmap = QPixmap('шистидий.png')
        scaled_pixmap = pixmap.scaled(QSize(60, 60),Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(scaled_pixmap)
        self.plant4.setIcon(icon)
        self.plant4.setIconSize(QSize(140, 140))
        self.plant4.setProperty("animal_name", "Антарктический мох")
        self.plant4.clicked.connect(self.btn)

        self.plant5.setStyleSheet("""QPushButton {
                background-color: transparent;
                border: none;}""")
        pixmap = QPixmap('бриум.png')
        scaled_pixmap = pixmap.scaled(QSize(60, 60),Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(scaled_pixmap)
        self.plant5.setIcon(icon)
        self.plant5.setIconSize(QSize(140, 140))
        self.plant5.setProperty("animal_name", "Псевдотриугольный бриум")
        self.plant5.clicked.connect(self.btn)

    def btn_style_station(self):
        self.station1.setStyleSheet("""QPushButton {
                        background-color: transparent;
                        border: none;}""")
        pixmap = QPixmap('черная.png')
        scaled_pixmap = pixmap.scaled(QSize(60, 60), Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(scaled_pixmap)
        self.station1.setIcon(icon)
        self.station1.setIconSize(QSize(140, 140))
        self.station1.setProperty("animal_name", "Станция Моусон")
        self.station1.clicked.connect(self.btn_station)

        self.station2.setStyleSheet("""QPushButton {
                        background-color: transparent;
                        border: none;}""")
        pixmap = QPixmap('красная.png')
        scaled_pixmap = pixmap.scaled(QSize(60, 60), Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(scaled_pixmap)
        self.station2.setIcon(icon)
        self.station2.setIconSize(QSize(140, 140))
        self.station2.setProperty("animal_name", "База Эсперанса")
        self.station2.clicked.connect(self.btn_station)

        self.station3.setStyleSheet("""QPushButton {
                        background-color: transparent;
                        border: none;}""")
        pixmap = QPixmap('красная.png')
        scaled_pixmap = pixmap.scaled(QSize(60, 60), Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(scaled_pixmap)
        self.station3.setIcon(icon)
        self.station3.setIconSize(QSize(140, 140))
        self.station3.setProperty("animal_name", "Станция Восток")
        self.station3.clicked.connect(self.btn_station)

        self.station4.setStyleSheet("""QPushButton {
                        background-color: transparent;
                        border: none;}""")
        pixmap = QPixmap('синяя.png')
        scaled_pixmap = pixmap.scaled(QSize(60, 60), Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(scaled_pixmap)
        self.station4.setIcon(icon)
        self.station4.setIconSize(QSize(140, 140))
        self.station4.setProperty("animal_name", "Станция Амундсен-Скотт")
        self.station4.clicked.connect(self.btn_station)

        self.station5.setStyleSheet("""QPushButton {
                        background-color: transparent;
                        border: none;}""")
        pixmap = QPixmap('синяя.png')
        scaled_pixmap = pixmap.scaled(QSize(60, 60), Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(scaled_pixmap)
        self.station5.setIcon(icon)
        self.station5.setIconSize(QSize(140, 140))
        self.station5.setProperty("animal_name", "Станция Мак-Мердо")
        self.station5.clicked.connect(self.btn_station)

    def btn(self):
        txt = self.sender().property("animal_name")
        self.object = Change_nature(txt)
        self.object.show()

    def btn_station(self):
        txt = self.sender().property("animal_name")
        self.object = Change_station(txt)
        self.object.show()


class Change_nature(QWidget):
    def __init__(self, who):
        try:
            super().__init__()
            self.setWindowTitle('Информация')
            f = io.StringIO(template_nature)
            uic.loadUi(f, self)
            self.setGeometry(500, 200, 740, 438)

            self.name_label.setText(who)
            self.name_label.adjustSize()
            self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.who = who
            self.baza()
            self.txt()
        except Exception as e:
            print(f"Ошибка восстановления: {e}")

    def baza(self):
        try:
            con = sqlite3.connect('arctic.db')
            cursor = con.cursor()
            cursor.execute(f"""SELECT description, image  FROM arctic_animals
                                    WHERE ru_name = '{self.who}'""")
            self.data = cursor.fetchall()
            self.data = self.data[0]
            self.description, self.image_path = self.data[0], self.data[1]
            con.close()
        except Exception as e:
            print(f"Ошибка восстановления: {e}")

    def txt(self):
        try:
            x = self.info_label.width()
            y = self.info_label.height()
            self.info_label.setText(self.description)
            self.info_label.adjustSize()
            self.info_label.resize(x, y)
            self.info_label.setWordWrap(True)

            pixmap = QPixmap(self.image_path[1:])
            scaled_pixmap = pixmap.scaled(self.photo_label.size(),
                                          Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation)
            self.photo_label.setPixmap(scaled_pixmap)
        except Exception as e:
            print(f"Ошибка восстановления: {e}")


class Change_station(QWidget):
    def __init__(self, who):
        try:
            super().__init__()
            self.setWindowTitle('Информация')
            f = io.StringIO(template_station)
            uic.loadUi(f, self)

            self.WEATHER_ICONS = {
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

            self.STATIONS = {
                1: {"name": "McMurdo", "coords": (-77.85, 166.67)},
                2: {"name": "Amundsen-Scott", "coords": (-84.99, 0.00)},
                3: {"name": "Vostok", "coords": (-78.46, 106.84)},
                4: {"name": "Esperanza", "coords": (-63.40, -57.00)},
                5: {"name": "Mouson", "coords": (-67.60, 62.87)}
            }

            self.YANDEX_API_KEY = "46cd6916-0196-4170-98ae-1f0350d88d67"
            self.BASE_URL = "https://api.weather.yandex.ru/v2/forecast"

            self.stationName_label.setText(who)
            self.stationName_label.adjustSize()
            self.stationName_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.who = who
            self.baza()
            self.txt()
        except Exception as e:
            print(f"Ошибка восстановления0: {e}")

    def get_weather(self, station_id):
        try:
            station = self.STATIONS[station_id]
            lat, lon = station["coords"]

            headers = {"X-Yandex-API-Key": self.YANDEX_API_KEY}
            params = {
                'lat': lat,
                'lon': lon,
                'lang': 'ru_RU',
                'limit': 1,
                'hours': 'false',
                'days': '1'
            }

            response = requests.get(self.BASE_URL, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            current = data['forecasts'][0]['parts']['day_short']
            temp = current['temp']
            feels_like = current.get('feels_like', temp)
            wind_speed = current['wind_speed']
            try:
                weather_desc = self.WEATHER_ICONS[current['condition']]

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
            return {'name': self.STATIONS[station_id]['name'], 'error': str(e)[:50]}

    def baza(self):
        try:
            con = sqlite3.connect('arctic_centres.db')
            cursor = con.cursor()
            cursor.execute(f"""SELECT description, image, wind, condition, pressure, humidity, temp
                                FROM arctic_centres
                                WHERE ru_name = '{self.who}'""")
            self.data = cursor.fetchall()
            self.data = self.data[0]
            self.description, self.image_path = self.data[0], self.data[1]
            self.wind, self.condition, self.pressure, self.humidity, self.temp = self.data[2:]
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
            con.commit()

            stations = []
            for station_id in self.STATIONS:
                weather = self.get_weather(station_id)
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
                    print(f"Ошибка для {self.STATIONS[station_id]['name']}: {weather['error']}")

            if stations:
                cursor.executemany('''
                        UPDATE arctic_centres 
                        SET condition = ?, temp = ?, pressure = ?, humidity = ?, wind = ?
                        WHERE id = ?
                    ''', stations)
                con.commit()

            con.close()
        except Exception as e:
            print(f"Ошибка восстановления1: {e}")


    def txt(self):
        try:
            x = self.stationInfo_label.width()
            y = self.stationInfo_label.height()
            self.stationInfo_label.setText(self.description)
            self.stationInfo_label.adjustSize()
            self.stationInfo_label.resize(x, y)
            self.stationInfo_label.setWordWrap(True)
            print(self.image_path)
            print(self.image_path[1:])
            pixmap = QPixmap(self.image_path[1:])
            print(self.image_path[1:])
            scaled_pixmap = pixmap.scaled(self.stationPhoto_label.size(),
                                          Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation)
            self.stationPhoto_label.setPixmap(scaled_pixmap)

            self.temperature_label.setText(self.temp)
            self.wind_label.setText(self.wind)
            self.humidity_label.setText(self.humidity)
            self.pressure_label.setText(self.pressure)
            self.condition_label.setText(self.condition)
        except Exception as e:
            print(f"Ошибка восстановления2: {e}")


class Way(QDialog):
    def __init__(self):
        try:
            super().__init__()
            self.setWindowTitle('Выбрать маршрут')
            f = io.StringIO(template_ways)
            uic.loadUi(f, self)

            self.dikt = {
                '-': 0,
                'Маршрут Джеймса Кука': 1,
                'Маршрут Беллинсгаузна и Лазарева': 2}
            self.save_btn.clicked.connect(self.on_accept)
        except Exception as e:
            print(f"Ошибка восстановления: {e}")

    def on_accept(self):
        try:
            self.result = self.ways_comboBox.currentIndex()
            self.accept()
        except Exception as e:
            print(f"Ошибка восстановления: {e}")

class Fakt(QWidget):
    def __init__(self):
        try:
            super().__init__()
            f = io.StringIO(template_fact)
            uic.loadUi(f, self)
            self.generate_button.pressed.connect(self.interesting_facts)
            self.setWindowTitle("Интересные факты")
            self.ai_answer_list = [1, 2, 3]
        except Exception as e:
            print(f"Ошибка восстановления: {e}")

    def interesting_facts(self):
        with GigaChat(credentials="MDE5YWVkODctZTkxYS03YWRlLThiZDQtNDdkOTIxY2E3OWM4OjBkYjdmZjY5LTJiZjAtNDg3Ny1hMTgyLTIyMDg1NzU3Njg0Yw==",
                verify_ssl_certs=False, model='GigaChat-Pro') as giga:
            response = giga.chat("Составь 3 интересных факта об Антарктике в одно предложение без кавычек и других лишних знаков. Раздели их новой строкой")
            print(response.choices[0].message.content)
            self.ai_answer_list = response.choices[0].message.content.split('\n')
            self.first_fact.setText(self.ai_answer_list[0].capitalize())
            self.second_fact.setText(self.ai_answer_list[1].capitalize())
            self.third_fact.setText(self.ai_answer_list[2].capitalize())


class QuizWindow(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template_quiz)
        uic.loadUi(f, self)
        self.setWindowTitle('Квиз')

        self.correct_buttons = {
            "answer1_3", "answer2_3", "answer3_4", "answer4_2", "answer5_2"
        }

        self.question_groups = {}
        self._setup_button_groups()

        self.end_btn.clicked.connect(self.finish_quiz)

        self.score_window = ScoreWindow(self)

    def _setup_button_groups(self):
        for i in range(1, 6):
            group = QButtonGroup(self)
            group.setExclusive(True)

            for j in range(1, 5):
                btn_name = f"answer{i}_{j}"
                btn = getattr(self, btn_name, None)
                if btn is not None:
                    group.addButton(btn)
                    self.question_groups[btn_name] = group

    def finish_quiz(self):
        score = 0
        total_questions = len(self.correct_buttons)


        for correct_btn_name in self.correct_buttons:
            btn = getattr(self, correct_btn_name, None)
            if btn is not None and btn.isChecked():
                score += 1


        self.score_window.set_score(score, total_questions)
        self.score_window.show()
        self.hide()

    def reset_quiz(self):
        for group in self.question_groups.values():
            group.setExclusive(False)
            for btn in group.buttons():
                btn.setChecked(False)
            group.setExclusive(True)
        self.show()


class ScoreWindow(QWidget):
    def __init__(self, quiz_window):
        super().__init__()
        f = io.StringIO(template_quiz_scores)
        uic.loadUi(f, self)
        self.setWindowTitle('Итоги квиза')
        self.quiz_window = quiz_window

        self.back_btn.clicked.connect(self.exit_app)
        self.again_btn.clicked.connect(self.try_again)

    def set_score(self, score: int, total: int):
        self.score_label.setText(f"{score}")

    def exit_app(self):
        self.close()

    def try_again(self):
        self.hide()
        self.quiz_window.reset_quiz()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Encyclopedia()
    window.show()
    sys.exit(app.exec())