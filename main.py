import pygame
import os
import sys

from CONSTANTS import *
sys.path.insert(1, "/Users/admin/Desktop/Game_project/core")
from movement_logic import *

def refresh(aimbox, model):
    WINDOW.fill(GREEN)
    WINDOW.blit(model, (aimbox.x, aimbox.y))
    pygame.display.update()

def main(): #main function (main loop) of out game
    global CHARACTER
    character_rectangle = pygame.Rect(0, 0, 115, 220)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        refresh(character_rectangle, CHARACTER)

    pygame.quit()

#calling the main function
if __name__ == "__main__": #checking that function called in the original file
    main()
