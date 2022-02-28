from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
import sys


class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('이미지 분류 AI')

        self.button1 = QPushButton('버튼 1')
        self.button2 = QPushButton('버튼 2')
        self.button3 = QPushButton('버튼 3')
        self.button4 = QPushButton('버튼 4')
        self.button5 = QPushButton('버튼 5')

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.button1, 0, 0, 1, 4)
        self.main_layout.addWidget(self.button2, 1, 0, 1, 2)
        self.main_layout.addWidget(self.button3, 1, 2, 1, 2)
        self.main_layout.addWidget(self.button4, 2, 0, 1, 1)
        self.main_layout.addWidget(self.button5, 2, 1, 1, 3)

        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())