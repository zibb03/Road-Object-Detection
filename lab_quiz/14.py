import model

import os
import numpy as np
import tensorflow as tf
# print(1)

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QFileDialog, QGroupBox, QLabel
from PyQt5.QtGui import QPixmap
import sys

Model = model.Model()

class_names = os.listdir('../classification_data')
# print(2)

class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.path = ''
        self.predict = ''
        self.image_label = QLabel(self)

        self.text_label = QLabel(self)
        self.text_label.setText(self.predict)

        self.button1 = QPushButton('데이터 불러오기')
        self.button1.clicked.connect(self.button1_click)
        self.button2 = QPushButton('모델 학습')
        self.button2.clicked.connect(self.button2_click)
        self.button3 = QPushButton('모델 저장')
        self.button3.clicked.connect(self.button3_click)
        self.button4 = QPushButton('모델 불러오기')
        self.button4.clicked.connect(self.button4_click)
        self.button5 = QPushButton('이미지 분류')
        self.button5.clicked.connect(self.button5_click)

        # self.image_label = QLabel(self)
        # pixmap = QPixmap(self.path)
        # self.image_label.setPixmap(pixmap)

        self.group_box1 = QGroupBox('메뉴')
        self.group_box2 = QGroupBox('이미지')
        self.group_box3 = QGroupBox('분류 예측')

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addWidget(self.button2)
        self.hbox_layout.addWidget(self.button3)
        self.hbox_layout.addWidget(self.button4)
        self.hbox_layout.addWidget(self.button5)

        self.vbox_layout1 = QVBoxLayout()
        self.vbox_layout1.addWidget(self.image_label)
        self.vbox_layout1.addStretch(1)
        self.vbox_layout2 = QVBoxLayout()
        self.vbox_layout2.addWidget(self.text_label)
        self.vbox_layout2.addStretch(1)

        self.group_box1.setLayout(self.hbox_layout)
        self.group_box2.setLayout(self.vbox_layout1)
        self.group_box3.setLayout(self.vbox_layout2)

        self.main_layout = QGridLayout()
        # y1, x1, y2, x2
        self.main_layout.addWidget(self.group_box1, 0, 0, 1, 4)
        self.main_layout.setRowStretch(1, 1)
        self.main_layout.addWidget(self.group_box2, 1, 0, 1, 3)
        self.main_layout.addWidget(self.group_box3, 1, 3, 1, 1)

        self.setLayout(self.main_layout)


    def button1_click(self):
        self.path, _ = QFileDialog.getOpenFileName(self, 'ABCD', '../data/images', 'Image Files (*.jpg *.png)')
        if self.path == '':
            print('취소')
        else:
            print('PATH:', self.path)
            pixmap = QPixmap(self.path)
            self.image_label.setPixmap(pixmap)


    def button2_click(self):
        # 모델 학습
        Model.load_data()
        Model.build()
        Model.train()
        print("모델 학습 완료")


    def button3_click(self):
        # 모델 저장
        Model.save()
        print("모델 저장 완료")


    def button4_click(self):
        # 모델 불러오기
        Model.load()
        print("모델 불러오기 완료")


    def button5_click(self):
        # 이미지 분류
        self.predict = Model.predict(self.path)
        # self.predict = np.argmax(predict)
        # return self.class_names[index]
        # print(self.predict[0])

        for i in range(len(self.predict[0])):
            self.predict[0][i] /= sum(self.predict[0])

        t = "\t"
        e = ""
        b = [f'{class_names[i]}:\t{t if len(class_names[i]) < 8 else e}{self.predict[0][i]:.2f}%' for i in range(len(class_names))]
        print(b)

        self.text_label.setText("\n".join(b))

        print("이미지 분류 완료")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    # print(3)
    classification_ai = ClassificationAI()
    classification_ai.show()
    # print(4)
    sys.exit(app.exec())