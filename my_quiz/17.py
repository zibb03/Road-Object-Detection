import yolov3

import cv2
import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QFileDialog, QGroupBox, QLabel
from PyQt5.QtGui import QPixmap
import sys

model = yolov3.YOLO_V3()

class_names = os.listdir('../classification_data')

class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('도로 객체 검출 AI')

        self.path = ''
        self.predict = ''
        self.image_label1 = QLabel(self)
        self.image_label2 = QLabel(self)

        self.text_label = QLabel(self)
        self.text_label.setText(self.predict)

        self.button1 = QPushButton('이미지 선택')
        self.button1.clicked.connect(self.button1_click)

        self.group_box1 = QGroupBox('메뉴')
        self.group_box2 = QGroupBox('원본 이미지')
        self.group_box3 = QGroupBox('사물 검출 결과')

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)

        self.vbox_layout1 = QVBoxLayout()
        self.vbox_layout1.addWidget(self.image_label1)
        self.vbox_layout1.addStretch(1)
        self.vbox_layout2 = QVBoxLayout()
        self.vbox_layout2.addWidget(self.image_label2)
        self.vbox_layout2.addStretch(1)

        self.group_box1.setLayout(self.hbox_layout)
        self.group_box2.setLayout(self.vbox_layout1)
        self.group_box3.setLayout(self.vbox_layout2)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.group_box1, 0, 0, 1, 4)
        self.main_layout.setRowStretch(1, 1)
        self.main_layout.addWidget(self.group_box2, 1, 0, 1, 2)
        self.main_layout.addWidget(self.group_box3, 1, 2, 1, 2)

        self.setLayout(self.main_layout)


    def button1_click(self):
        self.path, _ = QFileDialog.getOpenFileName(self, 'ABCD', '../data/images', 'Image Files (*.jpg *.png)')

        if self.path == '':
            print('취소')
        else:
            print('PATH:', self.path)

            pixmap1 = QPixmap(self.path)
            pixmap1 = pixmap1.scaled(pixmap1.width() // 2, pixmap1.height() // 2, Qt.IgnoreAspectRatio)

            self.image_label1.setPixmap(pixmap1)

            img = cv2.imread(self.path)
            model.build()
            model.load()
            result = model.predict(img)
            cv2.imwrite("../output/output.jpg", result)

            pixmap2 = QPixmap("../output/output.jpg")
            pixmap2 = pixmap2.scaled(pixmap2.width() // 2, pixmap2.height() // 2, Qt.IgnoreAspectRatio)
            self.image_label2.setPixmap(pixmap2)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())