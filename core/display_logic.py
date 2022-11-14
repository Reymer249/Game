import pygame
from CONSTANTS import *

def refresh(aimbox, model):
    WINDOW.fill(GREEN)
    WINDOW.blit(model, (aimbox.x, aimbox.y))
    pygame.display.update()
