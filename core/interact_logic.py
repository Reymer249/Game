import pygame
import CONSTANTS
from main import *
from CONSTANTS import *
from core.movement_logic import *

pygame.init()

text_font = pygame.font.SysFont(None, 30)

text_box_size = (10, 600, 500, 100)

# Location of problems, defined as invisible squares, that a player can interact if it approaches the coordinates
problem1_level1 = pygame.Rect(303, 145, 30, 30)
problem2_level1 = pygame.Rect(535, 295, 30, 30)
problem3_level1 = pygame.Rect(800, 330, 30, 30)
# Other levels





# In case you need to see those problem squares to visualize
#def drawObject(color, level):

    #if level == 1:
        #pygame.draw.rect(WINDOW, color, problem1_level1)
        #pygame.draw.rect(WINDOW, color, problem2_level1)
        #pygame.draw.rect(WINDOW, color, problem3_level1)




def drawOptions(opt1, opt2, opt3, collide, level):

    #Draws answer options boxes
    pygame.draw.rect(WINDOW, WHITE, opt1)
    pygame.draw.rect(WINDOW, WHITE, opt2)
    pygame.draw.rect(WINDOW, WHITE, opt3)

    #Detects which problems is currently approached and displays the possible answers (picutres/text) on the boxes, need to load the pictures in constant. There you can see dimensions aswell
    if level == 1:
        if collide == 1:
            WINDOW.blit(problem1_correct, (550, 600))
            WINDOW.blit(problem1_incorrect1, (700, 600))
            WINDOW.blit(problem1_incorrect2, (850, 600))
        if collide == 2:
            WINDOW.blit(problem2_incorrect2, (550, 600))
            WINDOW.blit(problem2_correct, (700, 600))
            WINDOW.blit(problem2_incorrect1, (850, 600))
        if collide == 3:
            WINDOW.blit(problem3_incorrect2, (550, 600))
            WINDOW.blit(problem3_incorrect1, (700, 600))
            WINDOW.blit(problem3_correct, (850, 600))

    # Other levels





def drawText(text):
    # drawing the  text box
    text_box = pygame.Rect(text_box_size)
    pygame.draw.rect(WINDOW, WHITE, text_box)
    pygame.draw.rect(WINDOW, BLACK, (10, 595, 500, 5)) # Top border
    pygame.draw.rect(WINDOW, BLACK, (5, 600, 5, 100)) # Left border
    pygame.draw.rect(WINDOW, BLACK, (510, 600, 5, 100)) # Right border
    pygame.draw.rect(WINDOW, BLACK, (10, 700, 500, 5)) # Bottom border


    #Displays text within the text box borders
    bkg = None
    y = text_box.top
    lineSpacing = -2
    while text:
        i = 1
        if y + 20 > text_box.bottom:
            break
        while text_font.size(text[:i])[0] < text_box.width and i < len(text):
            i += 1
        if i < len(text):
            i = text.rfind(' ', 0, i) + 1
        if bkg:
            comment = text_font.render(text[:i], True, BLACK, bkg)
            image.set_colorkey(bkg)
        else:
            comment = text_font.render(text[:i], False, BLACK)

        WINDOW.blit(comment, (text_box.left, y))
        y += 20 + lineSpacing

        text = text[i:]



def interact1(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, level, mistakes):

    #Detects collison with the invisible squares
    collideProblem1 = character_rectangle.colliderect(problem1_level1)
    collideProblem2 = character_rectangle.colliderect(problem2_level1)
    collideProblem3 = character_rectangle.colliderect(problem3_level1)
    point = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    text = ''
    color = 'RED'

    if level == 1:
        # While not near any problem
        if not collideProblem1 and not collideProblem2 and not collideProblem3:
            color = BLUE # When drawing the problem locations to visualize
            text = "Let's have a look! (Click and hold on 'TASK')"
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

        # Once all the problems are fixed
        if fixed_1 and fixed_2 and fixed_3:
            text = "HA! I've done it!"

    return text, color, fixed_1, fixed_2, fixed_3, mistakes


def task(keys_pressed, level, mistakes):
    point = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    mistake_count = "Lost points: " + str(mistakes)


    # Task box and collision
    box_coordinates = pygame.Rect(1073, 65, 55, 20)
    collide_task = box_coordinates.collidepoint(point)

    #When clicked, it fills the blackboard with white page, so we can describe the goal of the level
    if collide_task and click[0]:
        pygame.draw.rect(WINDOW, WHITE, (59, 59, 1074, 426))

        if level == 1:
            WINDOW.blit(level1_task, (60, 60))
            task_description = text_font.render("Fix the circuit diagram such that it realizes the given diagram. ", True, BLACK,)
            hint1 = text_font.render('F1 = AB’C’ + ABC’ + ABC', True, BLACK)
            hint2 = text_font.render('F2 = A’BC + AB’C + ABC', True, BLACK)
            mistake_text = text_font.render(mistake_count, True, RED)
            WINDOW.blit(mistake_text, (900, 410)) # Currently there is a problem cause it keeps adding +1 to mistake counts if mouse button is pressed down, so often it will add more than one :/
            WINDOW.blit(task_description, (65, 370))
            WINDOW.blit(hint1, (65, 410))
            WINDOW.blit(hint2, (65, 450))
            #Could add a grade in the end, once the level is completed. Take the mistakes and calcuate the grade and assign it A B C D F and write it on the task white page

            # Other levels

    # Draws the task box on so that it is on top of the white page
    pygame.draw.rect(WINDOW, WHITE, box_coordinates)
    task_text = text_font.render('TASK', True, BLACK,)
    WINDOW.blit(task_text, (1075,66))
    pygame.draw.rect(WINDOW, BLACK, (1070, 62, 58, 3)) # Top border
    pygame.draw.rect(WINDOW, BLACK, (1070, 65, 3, 23)) # Left border
    pygame.draw.rect(WINDOW, BLACK, (1128, 62, 3, 26)) # Right border
    pygame.draw.rect(WINDOW, BLACK, (1073, 85, 55, 3)) # Bottom border
