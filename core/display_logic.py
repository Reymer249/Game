import pygame
from CONSTANTS import *


def refresh(aimbox, model):
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(model, (aimbox.x, aimbox.y))
    pygame.display.update()
