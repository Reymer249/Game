import pygame
import CONSTANTS
from main import *
from CONSTANTS import *
from core.movement_logic import *
from interact_logic import *

problem1_level5 = pygame.Rect(303, 145, 30, 30)
problem2_level5 = pygame.Rect(535, 295, 30, 30)
problem3_level5 = pygame.Rect(800, 330, 30, 30)
problem4_level5 = pygame.Rect(200, 330, 30, 30)

def interact5(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, fixed_4, level, mistakes):

    #Detects collison with the invisible squares
    collideProblem1 = character_rectangle.colliderect(problem1_level5)
    collideProblem2 = character_rectangle.colliderect(problem2_level5)
    collideProblem3 = character_rectangle.colliderect(problem3_level5)
    collideProblem4 = character_rectangle.colliderect(problem4_level5)
    point = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

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
                opt1 = pygame.Rect(550, 600, 100, 100)
                opt2 = pygame.Rect(700, 600, 100, 100)
                opt3 = pygame.Rect(850, 600, 100, 100)
                drawOptions(opt1, opt2, opt3, 1, level) # Draws the answer options

                #Mouse over and click on answer
                collideAnswer1 = opt1.collidepoint(point)
                if collideAnswer1:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'That seems to be right'
                        fixed_1 = True

                collideAnswer2 = opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_1 = False
                        mistakes += 1

                collideAnswer3 = opt3.collidepoint(point)
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
                opt1 = pygame.Rect(550, 600, 100, 100)
                opt2 = pygame.Rect(700, 600, 100, 100)
                opt3 = pygame.Rect(850, 600, 100, 100)
                drawOptions(opt1, opt2, opt3, 2, level)

                #Mouse over and click on answer
                collideAnswer1 = opt1.collidepoint(point)
                if collideAnswer1:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_2 = False
                        mistakes += 1

                collideAnswer2 = opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'That seems to be right!'
                        fixed_2 = True

                collideAnswer3 = opt3.collidepoint(point)
                if collideAnswer3:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_2 = False
                        mistakes += 1

        # Once problem 2 is fixed
        elif collideProblem2 and fixed_2:
            text = 'Fixed!'

        # Problem 3
        if collideProblem3 and not fixed_3:
            text = "Something's off! It's seems that there is a part missing!"

            if collideProblem3 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'HMM, I need to name this OR gate'
                opt1 = pygame.Rect(550, 600, 100, 100)
                opt2 = pygame.Rect(700, 600, 100, 100)
                opt3 = pygame.Rect(850, 600, 100, 100)
                drawOptions(opt1, opt2, opt3, 3, level)

                #Mouse over and click on answer
                collideAnswer1 = opt1.collidepoint(point)
                if collideAnswer1:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_3 = False
                        mistakes += 1

                collideAnswer2 = opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_3 = False
                        mistakes += 1

                collideAnswer3 = opt3.collidepoint(point)
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
                opt1 = pygame.Rect(550, 600, 100, 100)
                opt2 = pygame.Rect(700, 600, 100, 100)
                opt3 = pygame.Rect(850, 600, 100, 100)
                drawOptions(opt1, opt2, opt3, 3, level)

                #Mouse over and click on answer
                collideAnswer1 = opt1.collidepoint(point)
                if collideAnswer1:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_3 = False
                        mistakes += 1

                collideAnswer2 = opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_3 = False
                        mistakes += 1

                collideAnswer3 = opt3.collidepoint(point)
                if collideAnswer3:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'That seems to be right!'
                        fixed_3 = True

        # Once problem 3 is fixed
        elif collideProblem4 and fixed_4:
            text = 'Fixed!'


        # Once all the problems are fixed
        if fixed_1 and fixed_2 and fixed_3 and fixed_4:
            text = "HA! I've done it!"

    return text, color, fixed_1, fixed_2, fixed_3, mistakes
