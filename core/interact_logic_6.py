import pygame
import CONSTANTS
from main import *
from CONSTANTS import *
from core.movement_logic import *
from core.interact_logic1 import *

problem1_level6 = pygame.Rect(350, 95, 30, 30)
problem2_level6 = pygame.Rect(455, 325, 30, 30)
problem3_level6 = pygame.Rect(660, 145, 30, 30)
problem4_level6 = pygame.Rect(990, 235, 30, 30)


def drawOptions(opt1, opt2, opt3, collide):

    #Draws answer options boxes
    pygame.draw.rect(WINDOW, WHITE, opt1)
    pygame.draw.rect(WINDOW, WHITE, opt2)
    pygame.draw.rect(WINDOW, WHITE, opt3)

    if collide == 1:
        WINDOW.blit(OPTION6_1_1, CORD_OPT1)
        WINDOW.blit(OPTION6_1_2, CORD_OPT2)
        WINDOW.blit(OPTION6_1_3, CORD_OPT3)
    if collide == 2:
        WINDOW.blit(OPTION6_2_1, CORD_OPT1)
        WINDOW.blit(OPTION6_2_2, CORD_OPT2)
        WINDOW.blit(OPTION6_2_3, CORD_OPT3)
    if collide == 3:
        WINDOW.blit(OPTION6_3_1, CORD_OPT1)
        WINDOW.blit(OPTION6_3_2, CORD_OPT2)
        WINDOW.blit(OPTION6_3_3, CORD_OPT3)
    if collide == 4:
        WINDOW.blit(OPTION6_4_1, CORD_OPT1)
        WINDOW.blit(OPTION6_4_2, CORD_OPT2)
        WINDOW.blit(OPTION6_4_3, CORD_OPT3)


def interact6(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, fixed_4, level, mistakes):

    #Detects collison with the invisible squares
    collideProblem1 = character_rectangle.colliderect(problem1_level6)
    collideProblem2 = character_rectangle.colliderect(problem2_level6)
    collideProblem3 = character_rectangle.colliderect(problem3_level6)
    collideProblem4 = character_rectangle.colliderect(problem4_level6)
    point = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    text = ''
    color = ''

    if level == 6:
        # While not near any problem
        if not collideProblem1 and not collideProblem2 and not collideProblem3 and not collideProblem4:
            color = BLUE # When drawing the problem locations to visualize
            text = "Oh, this bat! Here it is!!! But let's go to work. It's the last level, so let's make it quick."
        else:
            color = RED # When drawing the problem locations to visualize

        # Near problem 1
        if collideProblem1 and not fixed_1:
            text = "Hey, another wire gnaw through! Let's fix"

            if collideProblem1 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'From now one I hate bats. However, what would fit here?'
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 1) # Draws the answer options

                #Mouse over and click on answer
                collideAnswer1 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer1:
                    text = 'Simple red wire, I choose you!'
                    if click[0]:
                        text = 'Hehey!'
                        fixed_1 = True

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = "Capacitor. Let's make it even more complicated?"
                    if click[0]:
                        text = "Nah, I don't want to"
                        fixed_1 = False
                        mistakes += 1

                collideAnswer3 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer3:
                    text = 'Wire as well, but fancy one'
                    if click[0]:
                        text = "Nope, I don't want to risk. Who knows, maybe this wire can't withstand the voltage this memory array needs?"
                        fixed_1 = False
                        mistakes += 1

        # Once problem is fixed
        elif collideProblem1 and fixed_1:
            text = "Bat, please, be gone. I don't want to fix it again"

        # Problem 2
        if collideProblem2 and not fixed_2:
            text = "Something's off! Another ground is missing!"

            if collideProblem2 and keys_pressed[pygame.K_RETURN]:
                text = "We did it already, don't stuck on this one"
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 2)

                #Mouse over and click on answer
                collideAnswer1 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer1:
                    text = 'S1mple ground :D'
                    if click[0]:
                        text = 'Yay, for sure!'
                        fixed_2 = True
                        mistakes += 1

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Not so simple ground. I still know how useful I am with my comments ;)'
                    if click[0]:
                        text = 'No. It feels like not my day today'
                        fixed_2 = False
                        mistakes += 1

                collideAnswer3 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer3:
                    text = 'Maybe this one?'
                    if click[0]:
                        text = "For sure not"
                        fixed_2 = False
                        mistakes += 1

        # Once problem 2 is fixed
        elif collideProblem2 and fixed_2:
            text = 'Take my job!'

        # Problem 3
        if collideProblem3 and not fixed_3:
            text = "What can I see? Does something missing here?"

            if collideProblem3 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'HMM, connection lost...'
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 3)

                #Mouse over and click on answer
                collideAnswer1 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer1:
                    text = 'Wire. So many wires today...'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_3 = False
                        mistakes += 1

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Capacitor - always right option!'
                    if click[0]:
                        text = 'Nah, not today :('
                        fixed_3 = False
                        mistakes += 1

                collideAnswer3 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer3:
                    text = 'Capacitor is good, but charged capacitor is even better!'
                    if click[0]:
                        text = 'Yup, that is right'
                        fixed_3 = True

        # Once problem 3 is fixed
        elif collideProblem3 and fixed_3:
            text = 'Fixed, move on'

        if collideProblem4 and not fixed_4:
            text = "Problem again, I am here to help!"

            if collideProblem4 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'Hmm, and inbetween we will put...'
                drawOptions(CONSTANTS.opt1, CONSTANTS.opt2, CONSTANTS.opt3, 4)

                #Mouse over and click on answer
                collideAnswer1 = CONSTANTS.opt1.collidepoint(point)
                if collideAnswer1:
                    text = 'Ground?'
                    if click[0]:
                        text = 'Nope, not ground!'
                        fixed_4 = False
                        mistakes += 1

                collideAnswer2 = CONSTANTS.opt2.collidepoint(point)
                if collideAnswer2:
                    text = 'Capacitor..?'
                    if click[0]:
                        text = 'It worked out!'
                        fixed_4 = True

                collideAnswer3 = CONSTANTS.opt3.collidepoint(point)
                if collideAnswer3:
                    text = "Capacitor... but not connected. Let's try?"
                    if click[0]:
                        text = 'No, not right'
                        fixed_4 = False
                        mistakes += 1

        # Once problem 3 is fixed
        elif collideProblem4 and fixed_4:
            text = 'It was an easy one!'


        # Once all the problems are fixed
        if fixed_1 and fixed_2 and fixed_3 and fixed_4:
                text = "Voila! Get ready, Boss!!!"

    return text, color, fixed_1, fixed_2, fixed_3, fixed_4, mistakes
