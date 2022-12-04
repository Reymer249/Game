import pygame

import CONSTANTS

from core import menu_logic
from core.interact_logic import *
from core.interact_logic import interact
from core.movement_logic import *
from core.display_logic import *
from core.interact_logic_5 import *
import core.interact_logic_6 as il6
import core.interact_logic1 as il1

def main_menu(level):
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
            if level == 1:
                level1()
            elif level == 2:
                level2()
            elif level == 5:
                level5()
            elif level == 6:
                level6()
        elif to_do == "read":
            continue
        elif to_do == "exit":
            run = False

    pygame.quit()


def level1():  # main function of our game

    # defining variables used in main
    character_rectangle = pygame.Rect(950, 500, CONSTANTS.SCALE_WIDTH, CONSTANTS.SCALE_HEIGHT)
    mistakes = 0
    level = 1
    fixed_1 = False
    fixed_2 = False
    fixed_3 = False
    fixed_4 = True
    fixed_5 = True
    fixed_6 = True
    nxt = False
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

        if keys_pressed[pygame.K_q] and keys_pressed[pygame.K_ESCAPE]:
            main_menu(level)

        if fixed_1 and fixed_2 and fixed_3:
            nxt = True

        # changing the coordinates using the pygame buttons tracker
        character_rectangle.x, character_rectangle.y = movement(VELOCITY, character_rectangle, keys_pressed)
        # changing the model according to where character moves
        CONSTANTS.CHARACTER = turn(CONSTANTS.CHARACTER, keys_pressed)

        # interaction logic
        text, color, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, mistakes = il1.interact(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, level, mistakes)

        # refreshing the picture
        refresh(character_rectangle, CONSTANTS.CHARACTER, text, color, keys_pressed, level, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, mistakes, nxt)

        if nxt == True and character_rectangle.colliderect(DOOR_RECT):
            level2()

    pygame.quit()

def level2():  # main function of our game

    # I think can generally use this for each level function if it also has 3 problems, if more or less then might need a little tweaking,
    # I assume if there are less than 3 for others we can just define the fixed_3 as True from the beggining

    # defining variables used in main
    character_rectangle = pygame.Rect(950, 500, CONSTANTS.SCALE_WIDTH, CONSTANTS.SCALE_HEIGHT)
    mistakes = 0
    level = 2
    fixed_1 = False
    fixed_2 = False
    fixed_3 = False
    fixed_4 = False
    fixed_5 = False
    fixed_6 = False
    nxt = False
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

        if keys_pressed[pygame.K_q] and keys_pressed[pygame.K_ESCAPE]:
            main_menu(level)

        if fixed_1 and fixed_2 and fixed_3 and fixed_4 and fixed_5 and fixed_6:
            nxt = True

        # changing the coordinates using the pygame buttons tracker
        character_rectangle.x, character_rectangle.y = movement(VELOCITY, character_rectangle, keys_pressed)
        # changing the model according to where character moves
        CONSTANTS.CHARACTER = turn(CONSTANTS.CHARACTER, keys_pressed)

        # interaction logic
        text, color, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, mistakes = il1.interact(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, level, mistakes)

        # refreshing the picture
        refresh(character_rectangle, CONSTANTS.CHARACTER, text, color, keys_pressed, level, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, mistakes, nxt)

        if nxt == True and character_rectangle.colliderect(DOOR_RECT):
            level2()

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
    fixed_6 = True
    fixed_5 = True
    nxt = False
    text = ''
    color = ''
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

        if fixed_1 and fixed_2 and fixed_3 and fixed_4 and fixed_5 and fixed_6:
            nxt = True

        if keys_pressed[pygame.K_q] and keys_pressed[pygame.K_ESCAPE]:
            main_menu(level)

        if keys_pressed[pygame.K_q] and keys_pressed[pygame.K_ESCAPE]:
            main_menu()

        if fixed_1 and fixed_2 and fixed_3 and fixed_4:
            nxt = True

        # changing the coordinates using the pygame buttons tracker
        character_rectangle.x, character_rectangle.y = movement(VELOCITY, character_rectangle, keys_pressed)
        # changing the model according to where character moves
        CONSTANTS.CHARACTER = turn(CONSTANTS.CHARACTER, keys_pressed)

        # interaction logic
        text, color, fixed_1, fixed_2, fixed_3, fixed_4, mistakes = interact5(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, fixed_4, level, mistakes)

        # refreshing the picture
        refresh(character_rectangle, CONSTANTS.CHARACTER, text, color, keys_pressed, level, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, mistakes, nxt)

        if nxt == True and character_rectangle.colliderect(DOOR_RECT):
            level6()

    pygame.quit()

def level6():
    # defining variables used in main
    character_rectangle = pygame.Rect(950, 500, CONSTANTS.SCALE_WIDTH, CONSTANTS.SCALE_HEIGHT)
    mistakes = 0
    level = 6
    fixed_1 = False
    fixed_2 = False
    fixed_3 = False
    fixed_4 = False
    fixed_5 = True
    fixed_6 = True
    nxt = False
    text = ''
    color = ''
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

        if keys_pressed[pygame.K_q] and keys_pressed[pygame.K_ESCAPE]:
            main_menu(level)

        if fixed_1 and fixed_2 and fixed_3 and fixed_4:
            nxt = True

        # changing the coordinates using the pygame buttons tracker
        character_rectangle.x, character_rectangle.y = movement(VELOCITY, character_rectangle, keys_pressed)
        # changing the model according to where character moves
        CONSTANTS.CHARACTER = turn(CONSTANTS.CHARACTER, keys_pressed)

        # interaction logic
        text, color, fixed_1, fixed_2, fixed_3, fixed_4, mistakes = il6.interact6(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, fixed_4, level, mistakes)

        # refreshing the picture
        refresh(character_rectangle, CONSTANTS.CHARACTER, text, color, keys_pressed, level, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, mistakes, nxt)
        print(fixed_1, fixed_2, fixed_3, fixed_4)

    pygame.quit()

def final_level():  # main function of our game
    # defining variables used in main
    character_rectangle = pygame.Rect(0, 0, CONSTANTS.SCALE_WIDTH, CONSTANTS.SCALE_HEIGHT)
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
        text, option = finalInteract(character_rectangle, keys_pressed)

        # refreshing the picture
        refreshFinal(character_rectangle, CONSTANTS.CHARACTER, text, option, keys_pressed)

    pygame.quit()



# calling the main function
if __name__ == "__main__":
    level2()
