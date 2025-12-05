import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QButtonGroup


class QuizWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("quiz_main.ui", self)

        self.correct_buttons = {
            "answer1_3", "answer2_3", "answer3_4", "answer4_2", "answer5_2"
        }

        self.question_groups = {}
        self._setup_button_groups()

        self.end_btn.clicked.connect(self.finish_quiz)

        self.score_window = ScoreWindow(self)

    def _setup_button_groups(self):
        for i in range(1, 6):  # 5 вопросов
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
        uic.loadUi("quiz_scores.ui", self)
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
    window = QuizWindow()
    window.show()
    sys.exit(app.exec())