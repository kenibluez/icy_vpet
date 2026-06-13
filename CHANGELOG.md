# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased] - 2026-06-12

### Added
- **Movement System**: Implemented a state machine with `IDLE`, `WALKING`, and `SLEEPING` states.
- **Random Behaviors**: The pet now chooses random destinations to walk to and decides when to sleep.
- **Sprite Flipping**: The sprite now correctly faces the direction of movement.
- **Scaling Support**: Added the ability to scale sprites during loading; pet size reduced by 50%.
- **Initial Positioning**: The pet now spawns at the bottom of the screen, accounting for the taskbar.
- **Sprite Loader**: Initial implementation of a spritesheet loader compatible with Aseprite exports.
- **Basic Animation**: Implemented the core animation loop for the idle state.
- **Transparent Window**: Created the base `PetWindow` with transparency and "always on top" flags.

### Fixed
- **PySide6 Compatibility**: Fixed an `AttributeError` in `QPixmap.scaled` by using positional arguments instead of keywords.
