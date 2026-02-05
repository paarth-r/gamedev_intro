WIDTH = 1200
HEIGHT = 800
TILESIZE = 32

TITLE = "W game"
FPS = 60

# Player movement
PLAYER_ACCELERATION = 2000   # pixels per second^2
PLAYER_FRICTION = 2.0       # velocity decay per second (higher = stops faster)
PLAYER_MAX_SPEED = 2000      # pixels per second

# Enemy movement (cumbersome: accelerates fast, hard to stop)
ENEMY_ACCELERATION = 2800   # pixels per second^2
ENEMY_FRICTION = 0.9       # velocity decay per second (lower = can't stop easily)
ENEMY_MAX_SPEED = 2000      # pixels per second

BLUE = (0, 112, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
