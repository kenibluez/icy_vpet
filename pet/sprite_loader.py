import json

from PySide6.QtGui import QPixmap


class SpriteLoader:

    def __init__(self, png, metadata):

        self.sheet = QPixmap(png)

        with open(metadata, encoding="utf8") as f:
            self.data = json.load(f)

        self.frames = []

        self.load()

    def load(self):

        frame_data = self.data["frames"]

        for name in frame_data:

            frame = frame_data[name]["frame"]

            sprite = self.sheet.copy(frame["x"], frame["y"], frame["w"], frame["h"])

            self.frames.append(sprite)

    def get_frames(self):

        return self.frames
