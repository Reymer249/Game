import pygame
import os
import sys

from CONSTANTS import *
from core.movement_logic import *
from core.display_logic import *

def main():#main function of our game

    #defining variables used in main
    global CHARACTER
    character_rectangle = pygame.Rect(0, 0, 115, 220)
    clock = pygame.time.Clock()

    #main loop of our game
    run = True
    while run:
        clock.tick(FPS)#function to have stable FPS
        #checking for x button to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #refreshing picture
        refresh(character_rectangle, CHARACTER)

        #changing the coordinates using the pygame buttons tracker
        character_rectangle.x, character_rectangle.y = movement(VELOCITY, character_rectangle)
        #changing the model according to where character moves
        CHARACTER = turn()

    pygame.quit()

#calling the main function
if __name__ == "__main__": #checking that function called in the original file
    main()
