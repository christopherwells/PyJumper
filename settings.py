from os import path
# CONSTANTS
# game
TITLE = "Hello world!"
FPS = 60

# window
WIDTH, HEIGHT = 600, 800

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
PINK = (255, 0, 255)
YELLOW = (255, 255, 0)

# sprite specific
TILE_SIZE = 32

# player
PLAYER_ACC = 0.75
PLAYER_FRICTION = -0.11
PLAYER_GRAVITY = 0.6

# splash screen
BLOCK_LIST = [
    (0, HEIGHT - 32, WIDTH, 32),
    (WIDTH / 2 - 32, HEIGHT * 3 / 4, 100, 20),
    (125, HEIGHT - 320, 100, 20),
    (320, 450, 100, 20),
    (175, 300, 50, 20)]

# assets
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, "img")
