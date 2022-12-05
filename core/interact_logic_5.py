import pygame
import CONSTANTS
from main import *
from CONSTANTS import *
from core.movement_logic import *
from core.interact_logic1 import *

problem1_level5 = pygame.Rect(410, 145, 30, 30)
problem2_level5 = pygame.Rect(905, 140, 30, 30)
problem3_level5 = pygame.Rect(690, 310, 30, 30)
problem4_level5 = pygame.Rect(425, 370, 30, 30)


def drawOptions(opt1, opt2, opt3, collide):

    #Draws answer options boxes
    pygame.draw.rect(WINDOW, WHITE, opt1)
    pygame.draw.rect(WINDOW, WHITE, opt2)
    pygame.draw.rect(WINDOW, WHITE, opt3)

    if collide == 1:
        WINDOW.blit(OPTION5_1_1, CORD_OPT1)
        WINDOW.blit(OPTION5_1_2, CORD_OPT2)
        WINDOW.blit(OPTION5_1_3, CORD_OPT3)
    if collide == 2:
         WINDOW.blit(OPTION5_4_1, CORD_OPT1)
         WINDOW.blit(OPTION5_4_2, CORD_OPT2)
         WINDOW.blit(OPTION5_4_3, CORD_OPT3)
    if collide == 3:
        WINDOW.blit(OPTION5_3_1, CORD_OPT1)
        WINDOW.blit(OPTION5_3_2, CORD_OPT2)
        WINDOW.blit(OPTION5_3_3, CORD_OPT3)
    if collide == 4:
        WINDOW.blit(OPTION5_2_1, CORD_OPT1)
        WINDOW.blit(OPTION5_2_2, CORD_OPT2)
        WINDOW.blit(OPTION5_2_3, CORD_OPT3)

def interact5(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, fixed_4, level, mistakes):

    #Detects collison with the invisible squares
    collideProblem1 = character_rectangle.colliderect(problem1_level5)
    collideProblem2 = character_rectangle.colliderect(problem2_level5)
    collideProblem3 = character_rectangle.colliderect(problem3_level5)
    collideProblem4 = character_rectangle.colliderect(problem4_level5)
    point = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    text = ''
    color = ''

    if level == 5:
        # While not near any problem
        if not collideProblem1 and not collideProblem2 and not collideProblem3 and not collideProblem4:
            color = BLUE # When drawing the problem locations to visualize
            text = "I feel like a bee - working all day. I wish I could fly..."
        else:
            color = RED # When drawing the problem locations to visualize

        # Near problem 1
        if collideProblem1 and not fixed_1:
            text = "Wire is cut!"

            if collideProblem1 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'Where did we find a bat crazy enough to gnaw through the wires?'
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 1) # Draws the answer options

                #Mouse over and click on answer
                collideAnswer1 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer1:
                    text = 'Oh, capacitor, maybe it will help me?'
                    if click[0]:
                        text = 'Nope, it will not'
                        fixed_1 = False
                        mistakes += 1

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Simple one?'
                    if click[0]:
                        text = 'Yup!'
                        fixed_1 = True

                collideAnswer3 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer3:
                    text = 'What if I put my hand inbetween these parts...?'
                    if click[0]:
                        text = 'Oof, no. I will not do it for the second time'
                        fixed_1 = False
                        mistakes += 1

        # Once problem is fixed
        elif collideProblem1 and fixed_1:
            text = 'Just as it never happened!'

        # Problem 2
        if collideProblem2 and not fixed_2:
            text = "Let's look here as well"

            if collideProblem2 and keys_pressed[pygame.K_RETURN]:
                text = 'HMM, I need to put something inbetween...'
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 2)

                #Mouse over and click on answer
                collideAnswer2 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer2:
                    text = 'Capacitor... it may work out'
                    if click[0]:
                        text = 'Yey, it did!'
                        fixed_2 = True

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Some weird thing... Could I kill someone with it?'
                    if click[0]:
                        text = 'Nope, without weird stuff today :('
                        fixed_2 = False
                        mistakes += 1

                collideAnswer2 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer2:
                    text = "Maybe let's do it simple"
                    if click[0]:
                        text = "You are wrong again. But don't get upset, we still have a bunch of stuff to do ;D"
                        fixed_2 = False
                        mistakes += 1

        # Once problem 2 is fixed
        elif collideProblem2 and fixed_2:
            text = "Done! Let's move on to the next one"

        # Problem 3
        if collideProblem3 and not fixed_3:
            text = " *zip-zip* Something's missing!"

            if collideProblem3 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = "Ground, there is no ground. Let's fix it"
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 3)

                #Mouse over and click on answer
                collideAnswer1 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer1:
                    text = 'Oh, charged one...'
                    if click[0]:
                        text = "Nah, doesn't fit"
                        fixed_3 = False
                        mistakes += 1

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Maybe uncharged capacitor will work?'
                    if click[0]:
                        text = 'No, unfortunately'
                        fixed_3 = False
                        mistakes += 1

                collideAnswer3 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer3:
                    text = 'Just simple ground? We can try!'
                    if click[0]:
                        text = 'That seems to be right!'
                        fixed_3 = True

        # Once problem 3 is fixed
        elif collideProblem3 and fixed_3:
            text = 'Another one'

        if collideProblem4 and not fixed_4:
            text = "Ah? Another hole for our answer is here!"

            if collideProblem4 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'Numbers again... Are you kidding me?'
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 4)

                #Mouse over and click on answer
                collideAnswer1 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer1:
                    text = "One. It's a number one. I know that I am useful :D"
                    if click[0]:
                        text = 'Right!'
                        fixed_4 = True

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = "Zero (Two)"
                    if click[0]:
                        text = 'Nope, but it was a nice reference ;)'
                        fixed_4 = False
                        mistakes += 1

                collideAnswer3 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer3:
                    text = "2..? It's not funny"
                    if click[0]:
                        text = 'No! Really, what did you expect?'
                        fixed_4 = False
                        mistakes += 1

        # Once problem 3 is fixed
        elif collideProblem4 and fixed_4:
            text = 'Tick!'


        # Once all the problems are fixed
        if fixed_1 and fixed_2 and fixed_3 and fixed_4:
            text = "Wubba Lubba dub-dub "

    return text, color, fixed_1, fixed_2, fixed_3, fixed_4, mistakes
