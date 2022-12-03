import pygame

import CONSTANTS

from core import menu_logic
from core.movement_logic import *
from core.display_logic import *
from core.interact_logic_5 import *


def main_menu():
    # defining variables used in main
    start_button_rectangle = pygame.Rect((WIDTH//2 - BUTTON_WIDTH//2, 60), (BUTTON_WIDTH, BUTTON_HEIGHT))
    read_button_rectangle = pygame.Rect((WIDTH//2 - BUTTON_WIDTH//2, 280), (BUTTON_WIDTH, BUTTON_HEIGHT))
    exit_button_rectangle = pygame.Rect((WIDTH//2 - BUTTON_WIDTH//2, 500), (BUTTON_WIDTH, BUTTON_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)  # function to have stable FPS
        # checking for x button to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        refresh_main(start_button_rectangle, read_button_rectangle, exit_button_rectangle)

        to_do = menu_logic.check_mouse(start_button_rectangle, read_button_rectangle, exit_button_rectangle)

        if to_do == "start":
            level1()
        elif to_do == "read":
            continue
        elif to_do == "exit":
            run = False

    pygame.quit()

def level1():  # main function of our game

    # I think can generally use this for each level function if it also has 3 problems, if more or less then might need a little tweaking,
    # I assume if there are less than 3 for others we can just define the fixed_3 as True from the beggining

    # defining variables used in main
    character_rectangle = pygame.Rect(950, 500, CONSTANTS.SCALE_WIDTH, CONSTANTS.SCALE_HEIGHT)
    mistakes = 0
    level = 1
    fixed_1 = False
    fixed_2 = False
    fixed_3 = False
    fixed_4 = True
    clock = pygame.time.Clock()

    # main loop of our game
    run = True
    while run:
        clock.tick(FPS)  # function to have stable FPS
        # checking for x button to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # getting the keys pressed
        keys_pressed = pygame.key.get_pressed()

        # changing the coordinates using the pygame buttons tracker
        character_rectangle.x, character_rectangle.y = movement(VELOCITY, character_rectangle, keys_pressed)
        # changing the model according to where character moves
        CONSTANTS.CHARACTER = turn(CONSTANTS.CHARACTER, keys_pressed)

        # interaction logic
        text, color, fixed_1, fixed_2, fixed_3, mistakes = interact1(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, level, mistakes)

        # refreshing the picture
        refresh(character_rectangle, CONSTANTS.CHARACTER, text, color, keys_pressed, level, fixed_1, fixed_2, fixed_3, fixed_4, mistakes)

    pygame.quit()

def level5():
    # defining variables used in main
    character_rectangle = pygame.Rect(950, 500, CONSTANTS.SCALE_WIDTH, CONSTANTS.SCALE_HEIGHT)
    mistakes = 0
    level = 5
    fixed_1 = False
    fixed_2 = False
    fixed_3 = False
    fixed_4 = False
    clock = pygame.time.Clock()

    # main loop of our game
    run = True
    while run:
        clock.tick(FPS)  # function to have stable FPS
        # checking for x button to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # getting the keys pressed
        keys_pressed = pygame.key.get_pressed()

        # changing the coordinates using the pygame buttons tracker
        character_rectangle.x, character_rectangle.y = movement(VELOCITY, character_rectangle, keys_pressed)
        # changing the model according to where character moves
        CONSTANTS.CHARACTER = turn(CONSTANTS.CHARACTER, keys_pressed)

        # interaction logic
        text, color, fixed_1, fixed_2, fixed_3, mistakes = interact5(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, fixed_4, level, mistakes)

        # refreshing the picture
        refresh(character_rectangle, CONSTANTS.CHARACTER, text, color, keys_pressed, level, fixed_1, fixed_2, fixed_3, fixed_4, mistakes)

    pygame.quit()



# calling the main function
if __name__ == "__main__":
    level5()
