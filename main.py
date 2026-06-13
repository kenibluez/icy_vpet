from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QGuiApplication

from pet.sprite_loader import SpriteLoader
from pet.pet_window import PetWindow

app = QApplication([])

sprites = SpriteLoader("assets/icyfox.png", "assets/icyfox.json", scale=0.75)

fox = PetWindow(sprites.get_frames())

# Position at the bottom of the screen
screen = QGuiApplication.primaryScreen().availableGeometry()
fox_height = fox.sizeHint().height() or 64 # Fallback if not yet calculated
fox.move(
    screen.width() // 2,
    screen.height() - fox_height
)

fox.show()

app.exec()
