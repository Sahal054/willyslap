import pygame

WINDOW_NAME = "WILLY SLAP"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 700

FPS = 90
DRAW_FPS = True

# sizes
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)
TARGET_SIZES = (70, 58)
TARGET_SIZE_RANDOMIZE = (1,2) # for each new target, it will multiply the size with an random value between X and Y
PENALTY_TARGET_SIZES = (50, 50)
PENALTY_TARGET_SIZE_RANDOMIZE = (1.2, 1.5)

# drawing
DRAW_HITBOX = False # will draw all the hitbox

# animation
ANIMATION_SPEED = 0.08 # the frame of the objects will change

# difficulty
GAME_DURATION = 60 # the game will last X sec
TARGET_SPAWN_TIME = 1.5
TARGET_MOVE_SPEED = {"min": 1, "max": 5}
PENALTY_TARGET_PENALTY = 1 # will remove X of the score of the player 

# colors
COLORS = {"title": (38, 61, 39), "score": (38, 61, 39), "timer": (38, 61, 39),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (46, 54, 163)}} # second is the color when the mouse is on the button

# sounds / music
MUSIC_VOLUME = 0.13 # value between 0 and 1
SOUNDS_VOLUME = 1.5

# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
