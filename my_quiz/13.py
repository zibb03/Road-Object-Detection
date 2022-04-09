# QFileDialog

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QFileDialog, QGroupBox, QLabel
from PyQt5.QtGui import QPixmap
import sys


class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        # self.path = 0
        self.image_label = QLabel(self)

        self.button1 = QPushButton('파일 열기')
        self.button1.clicked.connect(self.button1_click)

        # self.image_label = QLabel(self)
        # pixmap = QPixmap(self.path)
        # self.image_label.setPixmap(pixmap)

        self.group_box1 = QGroupBox('그룹1')
        self.group_box2 = QGroupBox('그룹2')

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.image_label)

        self.group_box1.setLayout(self.hbox_layout)
        self.group_box2.setLayout(self.vbox_layout)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.group_box1, 0, 0, 1, 1)
        self.main_layout.addWidget(self.group_box2, 1, 0, 1, 1)

        self.setLayout(self.main_layout)


    def button1_click(self):
        path, _ = QFileDialog.getOpenFileName(self, 'ABCD', '../data/images', 'Image Files (*.jpg *.png)')
        if path == '':
            print('취소')
        else:
            print('PATH:', path)
            pixmap = QPixmap(path)
            self.image_label.setPixmap(pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())