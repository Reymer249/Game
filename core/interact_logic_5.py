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
            text = "Let's have a look!"
        else:
            color = RED # When drawing the problem locations to visualize

        # Near problem 1
        if collideProblem1 and not fixed_1:
            text = "Something's off! It's seems that there is a part missing!"

            if collideProblem1 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'HMM, It seems the circuit is not fully connected. I wonder fits in here'
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 1) # Draws the answer options

                #Mouse over and click on answer
                collideAnswer1 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer1:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_1 = False
                        mistakes += 1

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'That seems to be right'
                        fixed_1 = True

                collideAnswer3 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer3:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_1 = False
                        mistakes += 1

        # Once problem is fixed
        elif collideProblem1 and fixed_1:
            text = 'Fixed!'

        # Problem 2
        if collideProblem2 and not fixed_2:
            text = "Something's off! It's seems that there is a part missing!"

            if collideProblem2 and keys_pressed[pygame.K_RETURN]:
                text = 'HMM, I need to name this AND gate'
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 2)

                #Mouse over and click on answer
                collideAnswer2 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer2:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_2 = False
                        mistakes += 1

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_2 = False
                        mistakes += 1

                collideAnswer2 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer2:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'That seems to be right!'
                        fixed_2 = True

        # Once problem 2 is fixed
        elif collideProblem2 and fixed_2:
            text = 'Fixed!'

        # Problem 3
        if collideProblem3 and not fixed_3:
            text = "Something's off! It's seems that there is a part missing!"

            if collideProblem3 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'HMM, I need to name this OR gate'
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 3)

                #Mouse over and click on answer
                collideAnswer1 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer1:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_3 = False
                        mistakes += 1

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_3 = False
                        mistakes += 1

                collideAnswer3 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer3:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'That seems to be right!'
                        fixed_3 = True

        # Once problem 3 is fixed
        elif collideProblem3 and fixed_3:
            text = 'Fixed!'

        if collideProblem4 and not fixed_4:
            text = "Something's off! It's seems that there is a part missing!"

            if collideProblem4 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'HMM, I need to name this OR gate'
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 4)

                #Mouse over and click on answer
                collideAnswer1 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer1:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'That seems to be right!'
                        fixed_4 = True

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_4 = False
                        mistakes += 1

                collideAnswer3 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer3:
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_4 = False
                        mistakes += 1

        # Once problem 3 is fixed
        elif collideProblem4 and fixed_4:
            text = 'Fixed!'


        # Once all the problems are fixed
        if fixed_1 and fixed_2 and fixed_3 and fixed_4:
            text = "HA! I've done it!"

    return text, color, fixed_1, fixed_2, fixed_3, fixed_4, mistakes
