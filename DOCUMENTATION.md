# Foxy Documentation

This document provides a technical overview of the features implemented in the Foxy desktop pet project.

## Core Features

### 1. Transparent Desktop Window
- **File:** `pet/pet_window.py` (`PetWindow` class)
- **Implementation:** 
    - Uses `PySide6.QtWidgets.QLabel` as the base class.
    - Window flags set to `FramelessWindowHint`, `WindowStaysOnTopHint`, and `Tool`.
    - Attribute `WA_TranslucentBackground` is enabled to allow transparency.
    - CSS styling `background: transparent;` ensures the widget itself doesn't render a background.

### 2. Sprite Animation System
- **File:** `pet/sprite_loader.py` (`SpriteLoader` class), `pet/pet_window.py` (`animate` method)
- **Implementation:**
    - `SpriteLoader` reads an Aseprite-generated JSON metadata file and a corresponding PNG spritesheet.
    - Individual frames are extracted using `QPixmap.copy` based on coordinates in the JSON.
    - Supports a `scale` factor to resize sprites during loading using `QPixmap.scaled`.
    - `PetWindow.animate` cycles through frames using a `QTimer` (default 100ms).

### 3. Movement System & State Machine
- **File:** `pet/pet_window.py`
- **Implementation:**
    - **States:** `IDLE`, `WALKING`, `SLEEPING` (defined in `PetState` Enum).
    - **Logic:** `update_logic` (running every 1s) uses weighted random rolls to transition between states.
    - **Walking:** `choose_new_destination` picks a random X-coordinate on the screen. `update_position` (running at ~60FPS) increments the window's X-coordinate toward the target.
    - **Flipping:** The `animate` method uses `QTransform().scale(-1, 1)` to flip the sprite horizontally when the pet is moving left.

### 4. Screen Awareness & Positioning
- **File:** `main.py`
- **Implementation:**
    - Uses `QGuiApplication.primaryScreen().availableGeometry()` to detect the desktop area excluding the taskbar.
    - Positions the pet at the bottom of the screen by subtracting the pet's height from the screen height.

## Project Structure

```text
icy_vpet/
├── assets/             # Spritesheets and metadata
├── pet/
│   ├── pet_window.py   # Main window and logic controller
│   └── sprite_loader.py # Spritesheet parsing and processing
├── main.py             # Entry point
└── DEVELOPMENT_PLAN.md # Roadmap and progress tracking
```
