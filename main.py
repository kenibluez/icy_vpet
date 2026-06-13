from PySide6.QtWidgets import QApplication

from pet.sprite_loader import SpriteLoader
from pet.pet_window import PetWindow

app = QApplication([])

sprites = SpriteLoader("assets/icyfox.png", "assets/icyfox.json")

fox = PetWindow(sprites.get_frames())

fox.move(400, 400)

fox.show()

app.exec()
