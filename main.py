import pygame
import os
import sys

from CONSTANTS import *
sys.path.insert(1, "/Users/admin/Desktop/Game_project/core")
from movement_logic import *
def refresh(position, model):
    WINDOW.fill(GREEN)
    WINDOW.blit(model, (position.x, position.y))
    pygame.display.update()
    print(a)

def main(): #main function (main loop) of out game
    global CHARACTER
    character = pygame.Rect(0, 0, 115, 220)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] and character.y >= 0:
            character.y -= VELOCITY
        if keys_pressed[pygame.K_DOWN] and character.y <= 720-220:
            character.y += VELOCITY
        if keys_pressed[pygame.K_RIGHT] and character.x <= 1280-115:
            character.x += VELOCITY
            CHARACTER = CHARACTER_RIGHT
        if keys_pressed[pygame.K_LEFT] and character.x >= 0:
            character.x -= VELOCITY
            CHARACTER = CHARACTER_LEFT


        refresh(character, CHARACTER)

    pygame.quit()

if __name__ == "__main__": #checking that function called in the original file
    main()
