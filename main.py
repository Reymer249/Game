import CONSTANTS
from core.movement_logic import *
from core.display_logic import *

def main():#main function of our game

    #defining variables used in main
    character_rectangle = pygame.Rect(0, 0, CONSTANTS.SCALE_WIDTH, CONSTANTS.SCALE_HEIGHT)
    clock = pygame.time.Clock()

    #main loop of our game
    run = True
    while run:
        clock.tick(FPS)#function to have stable FPS
        #checking for x button to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #changing the coordinates using the pygame buttons tracker
        character_rectangle.x, character_rectangle.y = movement(VELOCITY, character_rectangle)
        #changing the model according to where character moves
        CONSTANTS.CHARACTER = turn(CONSTANTS.CHARACTER)


        #refreshing picture
        refresh(character_rectangle, CONSTANTS.CHARACTER)

    pygame.quit()

#calling the main function
if __name__ == "__main__":
    main()
