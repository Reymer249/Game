import pygame
from CONSTANTS import *
from core.interact_logic import *


def refresh(aimbox, model, text, color, keys_pressed, level, fixed_1, fixed_2, fixed_3, mistakes):


    # background (render 1st)
    WINDOW.blit(BACKGROUND, (0, 0))

    # levels on blackboard (render 2nd)
    if level == 1:


        if not fixed_1 and not fixed_2 and not fixed_3:
            WINDOW.blit(logic_array_broken, (100, 100))
        if fixed_1 and not fixed_2 and not fixed_3:
            WINDOW.blit(level1_fixed1, (100, 100))
        if not fixed_1 and fixed_2 and not fixed_3:
            WINDOW.blit(level1_fixed2, (100,100))
        if not fixed_1 and not fixed_2 and fixed_3:
            WINDOW.blit(level1_fixed3, (100,100))
        if fixed_1 and fixed_2 and not fixed_3:
            WINDOW.blit(level1_fixed1_fixed2, (100, 100))
        if fixed_1 and not fixed_2 and fixed_3:
            WINDOW.blit(level1_fixed1_fixed3, (100, 100))
        if not fixed_1 and fixed_2 and fixed_3:
            WINDOW.blit(level1_fixed2_fixed3, (100, 100))
        elif fixed_1 and fixed_2 and fixed_3:
            WINDOW.blit(logic_array_fixed, (100, 100))

    # Other levels

    # task (render 3rd)
    task(keys_pressed, level, mistakes)

    # character (render 4rd)
    WINDOW.blit(model, (aimbox.x, aimbox.y))

    # objects
    drawText(text)
    interact1(aimbox, keys_pressed, fixed_1, fixed_2, fixed_3, level, mistakes)

    pygame.display.update()



def refresh_main(start_rectangle, read_rectangle, exit_rectangle):
    WINDOW.fill(SOFT_BLUE)

    WINDOW.blit(START_BUTTON, (start_rectangle.x, start_rectangle.y))
    WINDOW.blit(READ_BUTTON, (read_rectangle.x, read_rectangle.y))
    WINDOW.blit(EXIT_BUTTON, (exit_rectangle.x, exit_rectangle.y))

    pygame.display.update()
