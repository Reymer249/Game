import pygame
from CONSTANTS import *
from core.interact_logic1 import *


def refresh(aimbox, model, text, color, keys_pressed, level, fixed_1, fixed_2, fixed_3, fixed_4, mistakes, nxt):


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
    if level == 5:
        if not fixed_1 and not fixed_2 and not fixed_3 and not fixed_4:
            WINDOW.blit(MEM_ARRAY5_BROKEN, (100, 100))
        if not fixed_1 and not fixed_2 and not fixed_3 and fixed_4:
            WINDOW.blit(MEM_ARRAY5_FIXED_4, (100, 100))
        if not fixed_1 and not fixed_2 and fixed_3 and not fixed_4:
            WINDOW.blit(MEM_ARRAY5_FIXED_3, (100, 100))
        if not fixed_1 and fixed_2 and not fixed_3 and not fixed_4:
            WINDOW.blit(MEM_ARRAY5_FIXED_2, (100, 100))
        if fixed_1 and not fixed_2 and not fixed_3 and not fixed_4:
            WINDOW.blit(MEM_ARRAY5_FIXED_1, (100, 100))
        if fixed_1 and fixed_2 and not fixed_3 and not fixed_4:
            WINDOW.blit(MEM_ARRAY5_FIXED_12, (100, 100))
        if fixed_1 and not fixed_2 and fixed_3 and not fixed_4:
            WINDOW.blit(MEM_ARRAY5_FIXED_13, (100, 100))
        if fixed_1 and not fixed_2 and not fixed_3 and fixed_4:
            WINDOW.blit(MEM_ARRAY5_FIXED_14, (100, 100))
        if not fixed_1 and fixed_2 and fixed_3 and not fixed_4:
            WINDOW.blit(MEM_ARRAY5_FIXED_23, (100, 100))
        if not fixed_1 and fixed_2 and not fixed_3 and fixed_4:
            WINDOW.blit(MEM_ARRAY5_FIXED_24, (100, 100))
        if not fixed_1 and not fixed_2 and fixed_3 and fixed_4:
            WINDOW.blit(MEM_ARRAY5_FIXED_34, (100, 100))
        if not fixed_1 and  fixed_2 and fixed_3 and not fixed_4:
            WINDOW.blit(MEM_ARRAY5_FIXED_123, (100, 100))
        if fixed_1 and fixed_2 and not fixed_3 and fixed_4:
            WINDOW.blit(MEM_ARRAY5_FIXED_124, (100, 100))
        if not fixed_1 and fixed_2 and fixed_3 and fixed_4:
            WINDOW.blit(MEM_ARRAY5_FIXED_234, (100, 100))
        if fixed_1 and not fixed_2 and fixed_3 and fixed_4:
            WINDOW.blit(MEM_ARRAY5_FIXED_134, (100, 100))
        if fixed_1 and fixed_2 and fixed_3 and fixed_4:
            WINDOW.blit(MEM_ARRAY5_FIXED_FULL, (100, 100))

    # task (render 3rd)
    task(keys_pressed, level, mistakes)

    # character (render 4rd)
    WINDOW.blit(model, (aimbox.x, aimbox.y))

    # objects
    drawText(text)
    if level == 1:
        interact1(aimbox, keys_pressed, fixed_1, fixed_2, fixed_3, level, mistakes)
    elif level == 5:
        interact5(aimbox, keys_pressed, fixed_1, fixed_2, fixed_3, fixed_4, level, mistakes)

    if nxt == True:
        WINDOW.blit(DOOR, (WIDTH - SCALE_WIDTH, HEIGHT - SCALE_HEIGHT))

    pygame.display.update()



def refresh_main(start_rectangle, read_rectangle, exit_rectangle):
    WINDOW.fill(SOFT_BLUE)

    WINDOW.blit(START_BUTTON, (start_rectangle.x, start_rectangle.y))
    WINDOW.blit(READ_BUTTON, (read_rectangle.x, read_rectangle.y))
    WINDOW.blit(EXIT_BUTTON, (exit_rectangle.x, exit_rectangle.y))

    pygame.display.update()
