# Vision

**Project Name:** Foxy (placeholder)

A desktop fox companion that:

* Lives on her desktop
* Has emotions and behaviors
* Reacts to her actions
* Reacts to music
* Can perform small computer tasks
* Contains personalized memories and messages

Think:

```text
Desktop Goose
+
Clippy
+
Tamagotchi
+
A scrapbook of your relationship
```

---

# Development Roadmap

## Phase 1 — Bring The Fox To Life

Goal:

```text
Make a fox exist on the desktop.
```

Nothing else.

### Features

* Transparent window
* Animated sprite
* Always on top
* Click-through support toggle
* Idle animation

### Tech

Since you're already familiar with PySide6:

```text
Python
PySide6
```

Structure:

```text
fox/
│
├── assets/
│   ├── idle/
│   ├── walk/
│   ├── sleep/
│
├── fox.py
├── animation.py
├── main.py
```

### Milestone

You launch the app.

A fox appears.

It animates.

Success.

---

## Phase 2 — Movement System

Goal:

```text
Fox moves around naturally.
```

### States

```text
Idle
Walking
Sleeping
Observing
```

State machine:

```text
         Idle
        /    \
   Walk      Sleep
        \    /
      Observe
```

### Behaviors

Randomly:

* Walk left
* Walk right
* Stop
* Sit
* Sleep

### Milestone

You can leave the fox running for an hour and it never feels broken.

---

## Phase 3 — Mouse Awareness

Goal:

```text
Fox notices the user.
```

### Features

* Detect cursor position
* Turn head toward cursor
* Follow cursor
* Run toward cursor

Potential interactions:

```text
Mouse close:
    Curious

Mouse moving:
    Watch

Mouse still:
    Sit nearby
```

### Milestone

The fox feels aware.

---

## Phase 4 — Personality System

This is where the magic starts.

Create:

```python
class Mood(Enum):
    HAPPY
    CURIOUS
    SLEEPY
    EXCITED
```

Mood influences:

* Movement speed
* Animation choice
* Speech bubbles

Example:

```text
Excited:
    Runs

Sleepy:
    Yawns

Curious:
    Follows mouse
```

---

## Phase 5 — Sound & Music

This is where your previous interest in WASAPI loopback becomes useful.

Goal:

```text
Fox reacts to computer audio output.
```

### MVP

Measure volume level.

```text
Quiet:
    Sleep

Loud:
    Excited
```

### Later

Beat detection:

```text
Beat detected:
    Jump

Bass hit:
    Tail wag

Music:
    Dance
```

### Architecture

```text
audio.py
```

Outputs:

```python
current_volume
beat_detected
```

The fox consumes those events.

---

## Phase 6 — Memory System

This is the gift part.

Create:

```text
memories.json
```

Example:

```json
{
  "name": "Sarah",
  "favorite_color": "purple",
  "anniversary": "2025-07-14"
}
```

The fox can say:

> Good morning Sarah.

> Happy anniversary ❤️

> Good luck today.

---

## Phase 7 — Fox Den

Double-click fox.

Open:

```text
Fox Den
```

Contents:

### Memories

Photos.

### Notes

Love letters.

### Achievements

```text
First date
Vacation
Birthday
```

### Journal

Messages you've written for her.

This is probably the feature she'll remember most.

---

## Phase 8 — Assistant Features

Now we add "Clippy".

Right-click fox:

```text
Open Spotify
Set Timer
Take Break
Focus Mode
Random Message
```

Possible integrations:

* Open websites
* Launch apps
* Volume control
* Reminders

Nothing destructive.

Only useful/cute actions.

---

# Architecture

I'd structure it like this:

```text
fox/
│
├── assets/
│
├── core/
│   ├── animation.py
│   ├── movement.py
│   ├── state_machine.py
│
├── systems/
│   ├── audio.py
│   ├── mouse.py
│   ├── memory.py
│
├── ui/
│   ├── fox_window.py
│   ├── fox_den.py
│
├── data/
│   ├── memories.json
│
└── main.py
```

---

# First Sprint (What I'd Build This Week)

### Day 1

* Transparent PySide6 window
* Fox sprite displayed

### Day 2

* Sprite animation system

### Day 3

* Movement system

### Day 4

* State machine

### Day 5

* Cursor tracking

### Day 6

* Basic personality system

### Day 7

* Packaging and testing

At the end of Week 1, you'll already have:

🦊 A fox that walks around the desktop, watches the cursor, sleeps, and feels alive.