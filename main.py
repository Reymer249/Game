import pygame

import CONSTANTS

from core import menu_logic
from core import read_menu_logic
from core.interact_logic import *
from core.interact_logic import interact
from core.movement_logic import *
from core.display_logic import *
from core.interact_logic_5 import *
import core.interact_logic_6 as il6
import core.interact_logic1 as il1
import core.interact_logic_3 as il3
import core.interact_logic_4 as il4


def read_menu(level):
    # defining variables used in main
    left_arrow_rectangle = pygame.Rect(
        (WIDTH // 2 - CONSTANTS.READMENU_ARROW_DIST,
         READMENU_SCREEN_PADDING + READMENU_SCREENSHOT_HEI // 2 - READMENU_ARROW_L.get_height() // 2),
        (READMENU_ARROW_L.get_width(),
         READMENU_ARROW_L.get_height()))
    right_arrow_rectangle = pygame.Rect(
        (WIDTH // 2 + READMENU_ARROW_DIST - READMENU_ARROW_R.get_width(),
         READMENU_SCREEN_PADDING + READMENU_SCREENSHOT_HEI // 2 - READMENU_ARROW_R.get_height() // 2),
        (READMENU_ARROW_R.get_width(),
         READMENU_ARROW_R.get_height()))
    exit_button_rectangle = pygame.Rect(
        (READMENU_SCREEN_PADDING, READMENU_SCREEN_PADDING),
        (READMENU_CROSS.get_width(), READMENU_CROSS.get_height()))
    clock = pygame.time.Clock()

    if_button_clicked = False

    slide = 0

    run = True
    while run:
        clock.tick(FPS)  # function to have stable FPS
        # checking for x button to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_read_menu(slide)

        to_do = read_menu_logic.check_mouse(left_arrow_rectangle, right_arrow_rectangle, exit_button_rectangle)

        if to_do == "none":
            if_button_clicked = False

        if not if_button_clicked:
            if to_do == "left":
                if slide > 0:
                    slide -= 1
                if_button_clicked = True
            elif to_do == "right":
                if slide < READMENU_SLIDECOUNT - 1:
                    slide += 1
                if_button_clicked = True
            elif to_do == "exit":
                main_menu(level)
                run = False

    pygame.quit()


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
            levels = [level1, level2, level3, level4, level5, level6, final_level]
            levels[level - 1]()
        elif to_do == "read":
            read_menu(level)
            run = False
        elif to_do == "exit":
            run = False

    pygame.quit()


def level1():  # main function of our game

    # defining variables used in main
    character_rectangle = pygame.Rect(950, 500, CONSTANTS.SCALE_WIDTH, CONSTANTS.SCALE_HEIGHT)
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

        if keys_pressed[pygame.K_ESCAPE]:
            main_menu(level)

        if fixed_1 and fixed_2 and fixed_3:
            nxt = True

        # changing the coordinates using the pygame buttons tracker
        character_rectangle.x, character_rectangle.y = movement(VELOCITY, character_rectangle, keys_pressed)
        # changing the model according to where character moves
        CONSTANTS.CHARACTER = turn(CONSTANTS.CHARACTER, keys_pressed)

        # interaction logic
        text, color, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, CONSTANTS.MISTAKES = il1.interact(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, level, CONSTANTS.MISTAKES)

        # refreshing the picture
        refresh(character_rectangle, CONSTANTS.CHARACTER, text, color, keys_pressed, level, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, CONSTANTS.MISTAKES, nxt)

        if nxt == True and character_rectangle.colliderect(DOOR_RECT):
            level2()
            run = False

    pygame.quit()


def level2():  # main function of our game

    # I think can generally use this for each level function if it also has 3 problems, if more or less then might need a little tweaking,
    # I assume if there are less than 3 for others we can just define the fixed_3 as True from the beggining

    # defining variables used in main
    character_rectangle = pygame.Rect(950, 500, CONSTANTS.SCALE_WIDTH, CONSTANTS.SCALE_HEIGHT)
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

        if keys_pressed[pygame.K_ESCAPE]:
            main_menu(level)

        if fixed_1 and fixed_2 and fixed_3 and fixed_4 and fixed_5 and fixed_6:
            nxt = True

        # changing the coordinates using the pygame buttons tracker
        character_rectangle.x, character_rectangle.y = movement(VELOCITY, character_rectangle, keys_pressed)
        # changing the model according to where character moves
        CONSTANTS.CHARACTER = turn(CONSTANTS.CHARACTER, keys_pressed)

        # interaction logic
        text, color, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, CONSTANTS.MISTAKES = il1.interact(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, level, CONSTANTS.MISTAKES)

        # refreshing the picture
        refresh(character_rectangle, CONSTANTS.CHARACTER, text, color, keys_pressed, level, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, CONSTANTS.MISTAKES, nxt)

        if nxt == True and character_rectangle.colliderect(DOOR_RECT):
            level3()
            run = False

    pygame.quit()


def level3():
    # defining variables used in main
    character_rectangle = pygame.Rect(950, 500, CONSTANTS.SCALE_WIDTH, CONSTANTS.SCALE_HEIGHT)
    level = 3
    fixed_1 = False
    fixed_2 = False
    fixed_3 = False
    fixed_4 = True
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

        if keys_pressed[pygame.K_ESCAPE]:
            main_menu(level)

        # changing the coordinates using the pygame buttons tracker
        character_rectangle.x, character_rectangle.y = movement(VELOCITY, character_rectangle, keys_pressed)
        # changing the model according to where character moves
        CONSTANTS.CHARACTER = turn(CONSTANTS.CHARACTER, keys_pressed)

        # interaction logic
        text, color, fixed_1, fixed_2, fixed_3, CONSTANTS.MISTAKES = il3.interact3(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, level, CONSTANTS.MISTAKES)

        # refreshing the picture
        refresh(character_rectangle, CONSTANTS.CHARACTER, text, color, keys_pressed, level, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, CONSTANTS.MISTAKES, nxt)
        if nxt == True and character_rectangle.colliderect(DOOR_RECT):
            level4()
            run = False

    pygame.quit()

def level4():
    # defining variables used in main
    character_rectangle = pygame.Rect(950, 500, CONSTANTS.SCALE_WIDTH, CONSTANTS.SCALE_HEIGHT)
    level = 4
    fixed_1 = False
    fixed_2 = False
    fixed_3 = False
    fixed_4 = True
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

        if keys_pressed[pygame.K_ESCAPE]:
            main_menu(level)

        # changing the coordinates using the pygame buttons tracker
        character_rectangle.x, character_rectangle.y = movement(VELOCITY, character_rectangle, keys_pressed)
        # changing the model according to where character moves
        CONSTANTS.CHARACTER = turn(CONSTANTS.CHARACTER, keys_pressed)

        # interaction logic
        text, color, fixed_1, fixed_2, fixed_3, CONSTANTS.MISTAKES = il4.interact4(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, level, CONSTANTS.MISTAKES)

        # refreshing the picture
        refresh(character_rectangle, CONSTANTS.CHARACTER, text, color, keys_pressed, level, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, CONSTANTS.MISTAKES, nxt)
        if nxt == True and character_rectangle.colliderect(DOOR_RECT):
            level5()
            run = False

    pygame.quit()


def level5():
    # defining variables used in main
    character_rectangle = pygame.Rect(950, 500, CONSTANTS.SCALE_WIDTH, CONSTANTS.SCALE_HEIGHT)
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

        if keys_pressed[pygame.K_ESCAPE]:
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
        text, color, fixed_1, fixed_2, fixed_3, fixed_4, CONSTANTS.MISTAKES = interact5(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, fixed_4, level, CONSTANTS.MISTAKES)

        # refreshing the picture
        refresh(character_rectangle, CONSTANTS.CHARACTER, text, color, keys_pressed, level, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, CONSTANTS.MISTAKES, nxt)

        if nxt == True and character_rectangle.colliderect(DOOR_RECT):
            level6()
            run = False

    pygame.quit()


def level6():
    # defining variables used in main
    character_rectangle = pygame.Rect(950, 500, CONSTANTS.SCALE_WIDTH, CONSTANTS.SCALE_HEIGHT)
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

        if keys_pressed[pygame.K_ESCAPE]:
            main_menu(level)

        if fixed_1 and fixed_2 and fixed_3 and fixed_4:
            nxt = True

        # changing the coordinates using the pygame buttons tracker
        character_rectangle.x, character_rectangle.y = movement(VELOCITY, character_rectangle, keys_pressed)
        # changing the model according to where character moves
        CONSTANTS.CHARACTER = turn(CONSTANTS.CHARACTER, keys_pressed)

        # interaction logic
        text, color, fixed_1, fixed_2, fixed_3, fixed_4, CONSTANTS.MISTAKES = il6.interact6(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, fixed_4, level, CONSTANTS.MISTAKES)

        # refreshing the picture
        refresh(character_rectangle, CONSTANTS.CHARACTER, text, color, keys_pressed, level, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, CONSTANTS.MISTAKES, nxt)
        if nxt == True and character_rectangle.colliderect(DOOR_RECT):
            final_level()
            run = False

    pygame.quit()


def final_level():
    # defining variables used in main
    character_rectangle = pygame.Rect(0, 0, CONSTANTS.SCALE_WIDTH, CONSTANTS.SCALE_HEIGHT)
    clock = pygame.time.Clock()
    level = 7

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

        if keys_pressed[pygame.K_ESCAPE]:
            main_menu(level)

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
    main_menu(1)
