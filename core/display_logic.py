import pygame
from CONSTANTS import *
from core.interact_logic import *


def refresh(aimbox, model, text, color, keys_pressed):
    # background and character
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(model, (aimbox.x, aimbox.y))

    # objects
    drawObject(color)
    drawText(text)
    interact(aimbox, keys_pressed)

    pygame.display.update()

def refresh_main(start_rectangle, read_rectangle, exit_rectangle):
    WINDOW.fill(SOFT_BLUE)

    WINDOW.blit(START_BUTTON, (start_rectangle.x, start_rectangle.y))
    WINDOW.blit(READ_BUTTON, (read_rectangle.x, read_rectangle.y))
    WINDOW.blit(EXIT_BUTTON, (exit_rectangle.x, exit_rectangle.y))

    pygame.display.update()
