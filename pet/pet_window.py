from enum import Enum, auto
from random import randint, choice

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QGuiApplication, QTransform

from PySide6.QtWidgets import QLabel


class PetState(Enum):
    IDLE = auto()
    WALKING = auto()
    SLEEPING = auto()


class PetWindow(QLabel):

    def __init__(self, frames):

        super().__init__()

        self.frames = frames
        self.current_frame = 0

        # State management
        self.state = PetState.IDLE
        self.state_timer = 0 # Used for states with duration
        self.target_x = 400
        self.speed = 1
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

        # Timers
        self.animate_timer = QTimer()
        self.animate_timer.timeout.connect(self.animate)
        self.animate_timer.start(100)

        self.logic_timer = QTimer()
        self.logic_timer.timeout.connect(self.update_logic)
        self.logic_timer.start(1000)  # Logic check every second

        self.move_timer = QTimer()
        self.move_timer.timeout.connect(self.update_position)
        self.move_timer.start(16)  # ~60 FPS for smooth movement

        self.animate()

    def animate(self):

        if not self.frames:
            return

        frame = self.frames[self.current_frame]

        # Flip if facing left
        if not self.facing_right:
            transform = QTransform().scale(-1, 1)
            frame = frame.transformed(transform)

        self.setPixmap(frame)

        self.resize(
            frame.width(),
            frame.height()
        )

        self.current_frame += 1

        if self.current_frame >= len(self.frames):
            self.current_frame = 0

    def update_logic(self):
        """Randomly decide what to do next."""
        if self.state == PetState.IDLE:
            # If idle, maybe start walking or sleeping
            roll = randint(0, 10)
            if roll < 3:  # 30% chance to start walking
                self.choose_new_destination()
                self.state = PetState.WALKING
            elif roll < 4:  # 10% chance to go to sleep
                self.state = PetState.SLEEPING
                self.state_timer = randint(5, 15)  # Sleep for 5-15 seconds

        elif self.state == PetState.WALKING:
            # If walking, maybe stop randomly
            if randint(0, 10) < 1:  # 10% chance to stop walking
                self.state = PetState.IDLE

        elif self.state == PetState.SLEEPING:
            self.state_timer -= 1
            if self.state_timer <= 0:
                self.state = PetState.IDLE

    def choose_new_destination(self):

        screen = QGuiApplication.primaryScreen()
        screen_width = screen.geometry().width()

        # Choose a target X that isn't too close to the current one
        current_x = self.x()

        # Try to find a target that is at least 200 pixels away
        possible_targets = []
        if current_x > 300:
            possible_targets.append(randint(0, current_x - 200))
        if current_x < screen_width - 300:
            possible_targets.append(randint(current_x + 200, screen_width - self.width()))

        if possible_targets:
            self.target_x = choice(possible_targets)
        else:
            self.target_x = randint(0, screen_width - self.width())

    def update_position(self):
        if self.state != PetState.WALKING:
            return

        x = self.x()

        if abs(self.target_x - x) < self.speed:
            self.state = PetState.IDLE
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