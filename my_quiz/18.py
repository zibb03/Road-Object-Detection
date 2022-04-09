import yolov3

import cv2
import os

from PyQt5.QtCore import Qt, QUrl, QFileInfo
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QSlider, QStyle, QGridLayout, QFileDialog, QGroupBox, QLabel
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QPixmap
import sys

model = yolov3.YOLO_V3()
video = False

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

        self.button1 = QPushButton('영상 선택')
        self.button1.clicked.connect(self.button1_click)

        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        video_widget = QVideoWidget()
        self.media_player.setVideoOutput(video_widget)
        self.media_player.stateChanged.connect(self.media_state_changed)
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)
        self.media_player.error.connect(self.handle_error)

        self.play_button = QPushButton()
        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.play_button.clicked.connect(self.play_video)

        self.position_slider = QSlider(Qt.Horizontal)
        self.position_slider.setRange(0, 0)
        self.position_slider.sliderMoved.connect(self.set_position)

        control_layout = QHBoxLayout()
        control_layout.addWidget(self.play_button)
        control_layout.addWidget(self.position_slider)

        self.group_box1 = QGroupBox('메뉴')
        self.group_box2 = QGroupBox('영상')

        self.hbox_layout1 = QHBoxLayout()
        self.hbox_layout1.addWidget(self.button1)
        self.hbox_layout2 = QHBoxLayout()
        self.hbox_layout2.addWidget(self.play_button)
        self.hbox_layout2.addWidget(self.position_slider)

        # print(video)
        # if video:
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(QFileInfo('../outputs/output.wmv').absoluteFilePath())))

        self.group_box1.setLayout(self.hbox_layout1)
        self.group_box2.setLayout(self.hbox_layout2)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.group_box1, 0, 0, 1, 4)
        self.main_layout.setRowStretch(1, 1)
        self.main_layout.addWidget(self.group_box2, 1, 0, 1, 4)

        self.setLayout(self.main_layout)


    def button1_click(self):
        global video
        self.path, _ = QFileDialog.getOpenFileName(self, 'ABCD', '../data/videos')

        if self.path == '':
            print('취소')
        else:
            print('PATH:', self.path)

            model.build()
            model.load()

            cap = cv2.VideoCapture(self.path)

            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

            if not os.path.exists('../outputs'):
                os.mkdir('../outputs')

            # print(fourcc, fps, width, height)
            out = cv2.VideoWriter('../outputs/output.wmv', fourcc, fps, (width, height))

            now_frame = 1

            while cap.isOpened():
                ret, image = cap.read()

                if not ret:
                    break

                result = model.predict(image)
                # cv2.imshow('image', img)
                # cv2.imshow('result', result)

                out.write(result)
                # if cv2.waitKey(1) == ord('q'):
                #     break

                print(f"{now_frame} / {frame_count}")
                now_frame += 1

            video = True

            cap.release()
            out.release()


    def play_video(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def media_state_changed(self, state):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self, position):
        self.position_slider.setValue(position)

    def duration_changed(self, duration):
        self.position_slider.setRange(0, duration)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def handle_error(self):
        print("Error: " + self.media_player.errorString())

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())