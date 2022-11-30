import pygame
from CONSTANTS import *
from core.interact_logic import *


def refresh(aimbox, model, text, color):
    WINDOW.blit(BACKGROUND, (0, 0))
    drawObject(color)
    WINDOW.blit(model, (aimbox.x, aimbox.y))
    drawText(text)
    interact(aimbox)
    pygame.display.update()
