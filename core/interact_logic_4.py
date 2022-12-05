import pygame
import CONSTANTS
from main import *
from CONSTANTS import *
from core.movement_logic import *
from core.interact_logic1 import *

problem1_level4 = pygame.Rect(565, 200, 115, 30)
problem2_level4 = pygame.Rect(120, 335, 30, 30)
problem3_level4 = pygame.Rect(365, 340, 30, 30)


def drawOptions(opt1, opt2, opt3, collide):

    #Draws answer options boxes
    pygame.draw.rect(WINDOW, WHITE, opt1)
    pygame.draw.rect(WINDOW, WHITE, opt2)
    pygame.draw.rect(WINDOW, WHITE, opt3)

    if collide == 1:
        WINDOW.blit(OPTION4_1_1, CORD_OPT1)
        WINDOW.blit(OPTION4_1_2, CORD_OPT2)
        WINDOW.blit(OPTION4_1_3, CORD_OPT3)
    if collide == 2:
         WINDOW.blit(OPTION4_2_1, CORD_OPT1)
         WINDOW.blit(OPTION4_2_2, CORD_OPT2)
         WINDOW.blit(OPTION4_2_3, CORD_OPT3)
    if collide == 3:
        WINDOW.blit(OPTION4_3_1, CORD_OPT1)
        WINDOW.blit(OPTION4_3_2, CORD_OPT2)
        WINDOW.blit(OPTION4_3_3, CORD_OPT3)

def interact4(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, level, mistakes):

    #Detects collison with the invisible squares
    collideProblem1 = character_rectangle.colliderect(problem1_level4)
    collideProblem2 = character_rectangle.colliderect(problem2_level4)
    collideProblem3 = character_rectangle.colliderect(problem3_level4)
    point = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    text = ''
    color = ''

    if level == 4:
        # While not near any problem
        if not collideProblem1 and not collideProblem2 and not collideProblem3:
            color = BLUE # When drawing the problem locations to visualize
            text = "Another level... bruh"
        else:
            color = RED # When drawing the problem locations to visualize

        # Near problem 1
        if collideProblem1 and not fixed_1:
            text = "Big part... missing! Ah, work again."

            if collideProblem1 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'It seems we need 4 numbers here'
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 1) # Draws the answer options

                #Mouse over and click on answer
                collideAnswer1 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer1:
                    text = '1101 is 13 in decimal. Not lucky number...'
                    if click[0]:
                        text = 'And... no :(('
                        fixed_1 = False
                        mistakes += 1

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'It looks fancy, wanna try this one?'
                    if click[0]:
                        text = 'Again no!?'
                        fixed_1 = False
                        mistakes += 1

                collideAnswer3 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer3:
                    text = "I don't like last options..."
                    if click[0]:
                        text = 'But this one is the right one!'
                        fixed_1 = True

        # Once problem is fixed
        elif collideProblem1 and fixed_1:
            text = 'Huh, another part done!'

        # Problem 2
        if collideProblem2 and not fixed_2:
            text = "Oops, it seems i need write something here as well"

            if collideProblem2 and keys_pressed[pygame.K_RETURN]:
                text = "Only one number, that's good. Less possibility for the mistake"
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 2)

                #Mouse over and click on answer
                collideAnswer2 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer2:
                    text = 'Just a number 0. Like a donut'
                    if click[0]:
                        text = 'That seems to be good!'
                        fixed_2 = True

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Number 1, I am always number 1'
                    if click[0]:
                        text = 'Nope, not right'
                        fixed_2 = False
                        mistakes += 1

                collideAnswer2 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer2:
                    text = 'Does two even can appear here..?'
                    if click[0]:
                        text = 'I was rejected'
                        fixed_2 = False
                        mistakes += 1

        # Once problem 2 is fixed
        elif collideProblem2 and fixed_2:
            text = 'Leading one in done'

        # Problem 3
        if collideProblem3 and not fixed_3:
            text = "Don't walk me away from this point. Let's firstly fix it!"

            if collideProblem3 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'Another day, another number missing...'
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 3)

                #Mouse over and click on answer
                collideAnswer1 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer1:
                    text = 'All in on zero!'
                    if click[0]:
                        text = "Bet didn't play"
                        fixed_3 = False
                        mistakes += 1

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = "1... and more dots to make you doubt.........."
                    if click[0]:
                        text = "You shouldn't trust me"
                        fixed_3 = True

                collideAnswer3 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer3:
                    text = '2, really? Why am I controlled by an idiot?...'
                    if click[0]:
                        text = 'No, for sure no!'
                        fixed_3 = False
                        mistakes += 1

        # Once problem 3 is fixed
        elif collideProblem3 and fixed_3:
            text = 'Thank you, next!'

        # Once all the problems are fixed
        if fixed_1 and fixed_2 and fixed_3:
            text = "My mother told me that I am a smart boy. Let's go on the next level!"

    return text, color, fixed_1, fixed_2, fixed_3, mistakes
