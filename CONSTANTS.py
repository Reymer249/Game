import pygame
import os

#  window
WIDTH, HEIGHT = 1280, 720  # resolution
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # applying resolution to the window
pygame.display.set_caption("Fixit")  # the caption that appears at the top of the window

#  background image
BACKGROUND = pygame.image.load(os.path.join("Assets", "background", "background.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

#  game flow setting
FPS = 60
VELOCITY = 5  # velocity of the character

#  background
GREEN = (0, 229, 0)

#  character models
CHARACTER_FRONT = pygame.image.load(os.path.join("Assets", "character", "front.png"))
CHARACTER_FRONT_RIGHT = pygame.image.load(os.path.join("Assets", "character", "front-right.png"))
CHARACTER_FRONT_LEFT = pygame.image.load(os.path.join("Assets", "character", "front-left.png"))
CHARACTER_BACK = pygame.image.load(os.path.join("Assets", "character", "back.png"))
CHARACTER_BACK_RIGHT = pygame.image.load(os.path.join("Assets", "character", "back-right.png"))
CHARACTER_BACK_LEFT = pygame.image.load(os.path.join("Assets", "character", "back-left.png"))
CHARACTER_LEFT_STAY = pygame.image.load(os.path.join("Assets", "character", "left-stay.png"))
CHARACTER_LEFT_WALK = pygame.image.load(os.path.join("Assets", "character", "left-walk.png"))
CHARACTER_RIGHT_STAY = pygame.image.load(os.path.join("Assets", "character", "right-stay.png"))
CHARACTER_RIGHT_WALK = pygame.image.load(os.path.join("Assets", "character", "right-walk.png"))


SCALE_WIDTH, SCALE_HEIGHT = 160, 200

def scale(character):
    return pygame.transform.scale(character, (SCALE_WIDTH, SCALE_HEIGHT))


CHARACTER_FRONT = scale(CHARACTER_FRONT)
CHARACTER_FRONT_RIGHT = scale(CHARACTER_FRONT_RIGHT)
CHARACTER_FRONT_LEFT = scale(CHARACTER_FRONT_LEFT)
CHARACTER_BACK = scale(CHARACTER_BACK)
CHARACTER_BACK_RIGHT = scale(CHARACTER_BACK_RIGHT)
CHARACTER_BACK_LEFT = scale(CHARACTER_BACK_LEFT)
CHARACTER_LEFT_STAY = scale(CHARACTER_LEFT_STAY)
CHARACTER_LEFT_WALK = scale(CHARACTER_LEFT_WALK)
CHARACTER_RIGHT_STAY = scale(CHARACTER_RIGHT_STAY)
CHARACTER_RIGHT_WALK = scale(CHARACTER_RIGHT_WALK)

CHARACTER = CHARACTER_FRONT

#  moving "constants"
PACE = 15
CHARACTER_UP = 0
CHARACTER_DOWN = 0
CHARACTER_RIGHT = 0
CHARACTER_LEFT = 0

# game objects
DOOR = pygame.image.load(os.path.join("Assets", "objects", "door.png"))
