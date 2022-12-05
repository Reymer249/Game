import pygame
import CONSTANTS
from main import *
from CONSTANTS import *
from core.movement_logic import *
from core.interact_logic1 import *

problem1_level3 = pygame.Rect(400, 180, 30, 30)
problem2_level3 = pygame.Rect(795, 230, 30, 30)
problem3_level3 = pygame.Rect(955, 315, 30, 30)


def drawOptions(opt1, opt2, opt3, collide):

    #Draws answer options boxes
    pygame.draw.rect(WINDOW, WHITE, opt1)
    pygame.draw.rect(WINDOW, WHITE, opt2)
    pygame.draw.rect(WINDOW, WHITE, opt3)

    if collide == 1:
        WINDOW.blit(OPTION3_1_1, CORD_OPT1)
        WINDOW.blit(OPTION3_1_2, CORD_OPT2)
        WINDOW.blit(OPTION3_1_3, CORD_OPT3)
    if collide == 2:
         WINDOW.blit(OPTION3_2_1, CORD_OPT1)
         WINDOW.blit(OPTION3_2_2, CORD_OPT2)
         WINDOW.blit(OPTION3_2_3, CORD_OPT3)
    if collide == 3:
        WINDOW.blit(OPTION3_3_1, CORD_OPT1)
        WINDOW.blit(OPTION3_3_2, CORD_OPT2)
        WINDOW.blit(OPTION3_3_3, CORD_OPT3)

def interact3(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, level, mistakes):

    #Detects collison with the invisible squares
    collideProblem1 = character_rectangle.colliderect(problem1_level3)
    collideProblem2 = character_rectangle.colliderect(problem2_level3)
    collideProblem3 = character_rectangle.colliderect(problem3_level3)
    point = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    text = ''
    color = ''

    if level == 3:
        # While not near any problem
        if not collideProblem1 and not collideProblem2 and not collideProblem3:
            color = BLUE # When drawing the problem locations to visualize
            text = "Let's do some calculations!"
        else:
            color = RED # When drawing the problem locations to visualize

        # Near problem 1
        if collideProblem1 and not fixed_1:
            text = "Yoy, something here is missing. Let's have a look..."

            if collideProblem1 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'Hmm, it seems we are missing a number. What do you think?'
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 1) # Draws the answer options

                #Mouse over and click on answer
                collideAnswer1 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer1:
                    text = 'Just a number 0'
                    if click[0]:
                        text = 'Nope, that does not seem right :('
                        fixed_1 = False
                        mistakes += 1

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Just a number 1'
                    if click[0]:
                        text = 'That seems to be right!'
                        fixed_1 = True

                collideAnswer3 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer3:
                    text = 'Just a number 2'
                    if click[0]:
                        text = 'Nope, that does not seem right :('
                        fixed_1 = False
                        mistakes += 1

        # Once problem is fixed
        elif collideProblem1 and fixed_1:
            text = 'Done!'

        # Problem 2
        if collideProblem2 and not fixed_2:
            text = "And also problem here!"

            if collideProblem2 and keys_pressed[pygame.K_RETURN]:
                text = 'Hmm, I need to put a number. Could you please help me?'
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 2)

                #Mouse over and click on answer
                collideAnswer2 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer2:
                    text = 'Maybe 0?'
                    if click[0]:
                        text = 'Yey!'
                        fixed_2 = True

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Is it 1?'
                    if click[0]:
                        text = 'Ah... no.'
                        fixed_2 = False
                        mistakes += 1

                collideAnswer2 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer2:
                    text = "It may be 2... or not..."
                    if click[0]:
                        text = "It's a pity, that does not fit :("
                        fixed_2 = False
                        mistakes += 1

        # Once problem 2 is fixed
        elif collideProblem2 and fixed_2:
            text = 'Easy!'

        # Problem 3
        if collideProblem3 and not fixed_3:
            text = "Hello there"

            if collideProblem3 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'In hexadecimal numerical system it would be...'
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 3)

                #Mouse over and click on answer
                collideAnswer1 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer1:
                    text = 'The first letter of the alphabet..?'
                    if click[0]:
                        text = 'Nope ;('
                        fixed_3 = False
                        mistakes += 1

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'I know that B itself equals to the 11 in decimal system...'
                    if click[0]:
                        text = 'Perfect!'
                        fixed_3 = True

                collideAnswer3 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer3:
                    text = 'C... like vitamin C'
                    if click[0]:
                        text = 'No!?'
                        fixed_3 = False
                        mistakes += 1

        # Once problem 3 is fixed
        elif collideProblem3 and fixed_3:
            text = 'Equation solved!'

        # Once all the problems are fixed
        if fixed_1 and fixed_2 and fixed_3:
            text = "Yaaaaahoooooo!!!"

    return text, color, fixed_1, fixed_2, fixed_3, mistakes
