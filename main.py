import pygame

import CONSTANTS

from core import menu_logic
from core.movement_logic import *
from core.display_logic import *


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
        text, color = interact(character_rectangle, keys_pressed)

        # refreshing the picture
        refresh(character_rectangle, CONSTANTS.CHARACTER, text, color, keys_pressed)

    pygame.quit()


# calling the main function
if __name__ == "__main__":
    main_menu()
