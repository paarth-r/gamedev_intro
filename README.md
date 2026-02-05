# W game

A small top-down chase game built with Pygame. The player (white) is pursued by an enemy (red). Movement uses momentum—you can juke the enemy so its inertia carries it past you.

## Requirements

- Python 3.10+
- [Pygame](https://www.pygame.org/) 2.0+

```bash
pip install pygame-ce
```

## Run

From the project directory:

```bash
python main.py
```

## Controls

| Key | Action |
|-----|--------|
| **Space** | Toggle control: mouse follow ↔ WASD |
| **W / A / S / D** | Move (when control is WASD) |
| **Mouse** | Player chases cursor (when control is mouse) |
| **/** | Toggle HUD (FPS, control mode, collision) |
| **Escape** or **Q** | Quit |

- **Mouse mode:** The player steers toward the cursor with the same momentum physics as the enemy.
- **WASD mode:** Hold keys to accelerate; release to coast. Walls bounce you back.

## How it works

- **Player & enemy** use steering + acceleration with friction and max speed, so movement has inertia.
- **Enemy** seeks the player with limited steering—it commits to its direction and can overshoot if you juke.
- **Walls** reflect velocity and acceleration so you bounce off the screen edges.

## Project structure

```
my_game/
├── main.py      # Game loop, window, events, draw
├── sprites.py   # Player and Enemy (movement, walls, collision)
├── settings.py  # Resolution, FPS, movement constants, colors
├── utils.py     # Cooldown helper (optional)
└── README.md
```

Tune movement in `settings.py`: acceleration, friction, and max speed for both player and enemy.
