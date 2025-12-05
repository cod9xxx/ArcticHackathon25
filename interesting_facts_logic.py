import sys
from gigachat import GigaChat

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QButtonGroup


class InterestingFactsWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("interesting_facts.ui", self)
        self.generate_button.pressed.connect(self.interesting_facts)
        self.setWindowTitle("Interesting Facts")
        self.ai_answer_list = [1, 2, 3]

    def interesting_facts(self):
        with GigaChat(credentials="MDE5YWVkODctZTkxYS03YWRlLThiZDQtNDdkOTIxY2E3OWM4OjBkYjdmZjY5LTJiZjAtNDg3Ny1hMTgyLTIyMDg1NzU3Njg0Yw==", verify_ssl_certs=False) as giga:
            response = giga.chat("Составь 3 интересных факта об Антарктике в одно предложение без кавычек и других лишних знаков. Раздели их новой строкой")
            print(response.choices[0].message.content)
            self.ai_answer_list = response.choices[0].message.content.split('\n')
            self.first_fact.setText(self.ai_answer_list[0])
            self.second_fact.setText(self.ai_answer_list[1])
            self.third_fact.setText(self.ai_answer_list[2])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InterestingFactsWindow()
    window.show()
    sys.exit(app.exec())