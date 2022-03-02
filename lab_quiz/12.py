from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QGridLayout, QGroupBox, QLabel
import sys


class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('이미지 분류 AI')

        self.number = 0
        self.text_label = QLabel(self)
        self.text_label.setText(str(self.number))

        self.group_box1 = QGroupBox('그룹1')
        self.group_box2 = QGroupBox('그룹2')

        self.button1 = QPushButton('-')
        self.button2 = QPushButton('+')

        self.button1.clicked.connect(self.button1_click)
        self.button2.clicked.connect(self.button2_click)

        self.hbox_layout1 = QHBoxLayout()
        self.hbox_layout2 = QHBoxLayout()

        self.hbox_layout1.addWidget(self.button1)
        self.hbox_layout1.addWidget(self.button2)

        self.hbox_layout2.addWidget(self.text_label)

        self.group_box1.setLayout(self.hbox_layout1)
        self.group_box2.setLayout(self.hbox_layout2)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.group_box1, 0, 0, 1, 1)
        self.main_layout.addWidget(self.group_box2, 1, 0, 1, 1)

        self.setLayout(self.main_layout)


    def button1_click(self):
        self.number -= 1
        self.text_label.setText(str(self.number))



    def button2_click(self):
        self.number += 1
        self.text_label.setText(str(self.number))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())