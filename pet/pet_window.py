from random import randint

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QGuiApplication

from PySide6.QtWidgets import QLabel


class PetWindow(QLabel):

    def __init__(self, frames):

        super().__init__()

        self.frames = frames
        self.current_frame = 0

        # Movement
        self.target_x = 400
        self.speed = 2

        self.facing_right = True

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        self.setStyleSheet(
            "background: transparent;"
        )

        self.animate_timer = QTimer()

        self.animate_timer.timeout.connect(
            self.animate
        )

        self.animate_timer.start(
            100
        )

        self.move_timer = QTimer()

        self.move_timer.timeout.connect(
            self.update_position
        )

        self.move_timer.start(
            16
        )

        self.choose_new_destination()

        self.animate()

    def animate(self):

        if not self.frames:
            return

        frame = self.frames[self.current_frame]

        # Flip if facing left
        if not self.facing_right:

            frame = frame.transformed(
                Qt.TransformationMode.FastTransformation
            )

        self.setPixmap(frame)

        self.resize(
            frame.width(),
            frame.height()
        )

        self.current_frame += 1

        if self.current_frame >= len(self.frames):
            self.current_frame = 0

    def choose_new_destination(self):

        screen = QGuiApplication.primaryScreen()

        width = screen.geometry().width()

        self.target_x = randint(
            0,
            width - self.width()
        )

    def update_position(self):

        x = self.x()

        if abs(self.target_x - x) < 5:

            self.choose_new_destination()
            return

        if x < self.target_x:

            x += self.speed
            self.facing_right = True

        else:

            x -= self.speed
            self.facing_right = False

        self.move(
            x,
            self.y()
        )