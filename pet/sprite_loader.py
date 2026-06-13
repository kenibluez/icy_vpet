import json

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap


class SpriteLoader:

    def __init__(self, png, metadata, scale=1.0):

        self.sheet = QPixmap(png)
        self.scale = scale

        with open(metadata, encoding="utf8") as f:
            self.data = json.load(f)

        self.frames = []

        self.load()

    def load(self):

        frame_data = self.data["frames"]

        for name in frame_data:

            frame = frame_data[name]["frame"]

            sprite = self.sheet.copy(frame["x"], frame["y"], frame["w"], frame["h"])

            if self.scale != 1.0:
                sprite = sprite.scaled(
                    int(sprite.width() * self.scale),
                    int(sprite.height() * self.scale),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )

            self.frames.append(sprite)

    def get_frames(self):

        return self.frames
