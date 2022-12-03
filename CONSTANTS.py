import pygame
import os

#  window
WIDTH, HEIGHT = 1280, 720  # resolution
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # applying resolution to the window
pygame.display.set_caption("Fixit")  # the caption that appears at the top of the window

#  background image
BACKGROUND = pygame.image.load(os.path.join("Assets", "background", "background.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

FINAL_BACKGROUND = pygame.image.load(os.path.join("Assets", "background", "final_background.png"))
FINAL_BACKGROUND = pygame.transform.scale(FINAL_BACKGROUND, (WIDTH, HEIGHT))
#  game flow setting
FPS = 60
VELOCITY = 5  # velocity of the character

#  colors
GREEN = (0, 229, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
SOFT_BLUE = (202, 228, 241)

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

BOSS_RIGHT = pygame.image.load(os.path.join("Assets", "boss", "boss_right.png"))
BOSS_LEFT = pygame.image.load(os.path.join("Assets", "boss", "boss_left.png"))
BOSS_WOOSH = pygame.image.load(os.path.join("Assets", "boss", "boss_woosh.png"))

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

BOSS_RIGHT = scale(BOSS_RIGHT)
BOSS_LEFT = scale(BOSS_LEFT)
BOSS_WOOSH = scale(BOSS_WOOSH)

#  moving "constants"
PACE = 15
CHARACTER_UP = 0
CHARACTER_DOWN = 0
CHARACTER_RIGHT = 0
CHARACTER_LEFT = 0

# general game objects
DOOR = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "objects", "door.png")),
                              (SCALE_WIDTH, SCALE_HEIGHT))
DOOR_RECT = pygame.Rect(WIDTH-SCALE_WIDTH, HEIGHT-SCALE_HEIGHT, WIDTH, HEIGHT)
opt1 = pygame.Rect(550, 600, 100, 100)
opt2 = pygame.Rect(700, 600, 100, 100)
opt3 = pygame.Rect(850, 600, 100, 100)

# main menu objects
BUTTON_WIDTH, BUTTON_HEIGHT = 440, 160
START_BUTTON = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "main_menu", "start.png")), (BUTTON_WIDTH, BUTTON_HEIGHT))
EXIT_BUTTON = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "main_menu", "exit.png")), (BUTTON_WIDTH, BUTTON_HEIGHT))
READ_BUTTON = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "main_menu", "read.png")), (BUTTON_WIDTH, BUTTON_HEIGHT))

#level1 assets
#BLACKBOARD SPRITES
logic_array_broken = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "logic-array-needfixing.png")), (1030, 380))
logic_array_fixed = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "logic-array level1 completed.png")), (1030, 380))



level1_fixed1 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "level1_fixed1.png")), (1030, 380))
level1_fixed2 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "level1_fixed2.png")), (1030, 380))
level1_fixed3 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "level1_fixed3.png")), (1030, 380))

level1_fixed1_fixed2 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "level1_fixed1_fixed2.png")), (1030, 380))

level1_fixed1_fixed3 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "level1_fixed1_fixed3.png")), (1030, 380))

level1_fixed2_fixed3 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "level1_fixed2_fixed3.png")), (1030, 380))



#ANSWER SPRITES
problem1_correct = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "problem1-correct.png")), (90, 90))
problem1_incorrect1 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "problem1-incorrect1.png")), (90, 90))
problem1_incorrect2 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "problem1-incorrect2.png")), (90, 90))

problem2_correct = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "problem2-correct.png")), (90, 90))
problem2_incorrect1 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "problem2-incorrect1.png")), (90, 90))
problem2_incorrect2 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "problem2-incorrect2.png")), (90, 90))
problem3_correct = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "problem3-correct.png")), (90, 90))
problem3_incorrect1 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "problem3-incorrect1.png")), (90, 90))
problem3_incorrect2 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "problem3-incorrect1.png")), (90, 90))

#TASK TABLE LEVEL 1
level1_task = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "level1", "level1_task.jpg")), (1030, 320))

#level5 assets
MEM_ARRAY5_BROKEN = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_not_fixed.png")), (1030, 320))
MEM_ARRAY5_FIXED_FULL = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_fixed.png")), (1030, 320))
MEM_ARRAY5_FIXED_1 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_1_1.png")), (1030, 320))
MEM_ARRAY5_FIXED_2 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_1_2.png")), (1030, 320))
MEM_ARRAY5_FIXED_1 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_1_1.png")), (1030, 320))
MEM_ARRAY5_FIXED_2 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_1_2.png")), (1030, 320))
MEM_ARRAY5_FIXED_3 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_1_3.png")), (1030, 320))
MEM_ARRAY5_FIXED_4 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_1_4.png")), (1030, 320))
MEM_ARRAY5_FIXED_34 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_2_1.png")), (1030, 320))
MEM_ARRAY5_FIXED_24 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_2_2.png")), (1030, 320))
MEM_ARRAY5_FIXED_14 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_2_3.png")), (1030, 320))
MEM_ARRAY5_FIXED_12 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_2_4.png")), (1030, 320))
MEM_ARRAY5_FIXED_13 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_2_5.png")), (1030, 320))
MEM_ARRAY5_FIXED_23 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_2_6.png")), (1030, 320))
MEM_ARRAY5_FIXED_234 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_3_1.png")), (1030, 320))
MEM_ARRAY5_FIXED_123 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_3_2.png")), (1030, 320))
MEM_ARRAY5_FIXED_124 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_3_3.png")), (1030, 320))
MEM_ARRAY5_FIXED_134 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", 'level5', "lvl_5_3_4.png")), (1030, 320))

QUESTIONS = {("SRAMS are faster than DRAMS", "True", "False", "Depends on the task"): 1,
             ("PROMs are more expensive than EPROMs and EEPOMs", "True", "False", "They are the same price"): 2,
             ("What is an advantages of programmable logic devices over fixed logic devices?", "They can be mass produced more economically", "Can use inexpensive software tools to quickly validate the design", "Preferred in applications that require high performance level"): 2,
             ("Do the following calculation in binary:1001 - 101", "100", "001", "110"): 1,
             ("How does uv light affect EPROM?", "Creates an electro-magnetic field that erases the bit state", "Heats up the cell resulting in voltage generation", "Hits out electrons from floating gate transistors"): 3}
