import time

import pygame
from pygame import image

import CONSTANTS
from CONSTANTS import *
from core.movement_logic import *

pygame.init()


text_font = pygame.font.SysFont(None, 30)

#Coordinates and sizes
text_box_size = (10, 600, 500, 100)

simulator_rect = pygame.Rect(200, 125, 30, 30)


answer1_rect = pygame.Rect(600, 100, 500, 50)
answer2_rect = pygame.Rect(600, 200, 500, 50)
answer3_rect = pygame.Rect(600, 300, 500, 50)

points = 0
question_number = 0
answer1, answer2, answer3, text, answer, number = [], [], [], [], [], 0


def drawObject(color):
    pygame.draw.rect(WINDOW, color, simulator_rect)


def drawOptions(opt1, opt2, opt3):

    pygame.draw.rect(WINDOW, WHITE, opt1)
    pygame.draw.rect(WINDOW, WHITE, opt2)
    pygame.draw.rect(WINDOW, WHITE, opt3)


def drawText(text):
    # drawing the  text box
    text_box = pygame.Rect(text_box_size)
    pygame.draw.rect(WINDOW, WHITE, text_box)
    pygame.draw.rect(WINDOW, BLACK, (10, 595, 500, 5))  # Top border
    pygame.draw.rect(WINDOW, BLACK, (5, 600, 5, 100))  # Left border
    pygame.draw.rect(WINDOW, BLACK, (510, 600, 5, 100))  # Right border
    pygame.draw.rect(WINDOW, BLACK, (10, 700, 500, 5))  # Bottom border

    # Displays text within the text box borders
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



def customDrawText(text, x, y):
    # drawing the  text box
    text_box = pygame.Rect(x+5, y, 500, 50)
    pygame.draw.rect(WINDOW, WHITE, text_box)
    pygame.draw.rect(WINDOW, BLACK, (x, y-5, 500, 5)) # Top border
    pygame.draw.rect(WINDOW, BLACK, (x, y, 5, 50)) # Left border
    pygame.draw.rect(WINDOW, BLACK, (x+500, y, 5, 50)) # Right border
    pygame.draw.rect(WINDOW, BLACK, (x, y+50, 500, 5)) # Bottom border


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

    return text_box

def interact(character_rectangle, keys_pressed):
    collideProblem = character_rectangle.colliderect(simulator_rect)
    point = pygame.mouse.get_pos()

    # Objects changes color once the character is in distance
    if not collideProblem:
        color = BLUE
        text = "Let's have a look!"
    else:
        color = RED
        text = "Hmm, something's off! It's seems that there is a part missing!"

    if collideProblem and keys_pressed[pygame.K_RETURN]:
        text = 'EXPLAINING THE PROBLEM (LALALA THIS AND THAT)'
        opt1 = pygame.Rect(550, 600, 100, 100)
        opt2 = pygame.Rect(700, 600, 100, 100)
        opt3 = pygame.Rect(850, 600, 100, 100)
        drawOptions(opt1, opt2, opt3)

        collideAnswer1 = opt1.collidepoint(point)
        if collideAnswer1:
            text = 'HMM, Possibly (Explain this answer) OPT 1'

        collideAnswer2 = opt2.collidepoint(point)
        if collideAnswer2:
            text = 'HMM, Possibly (Explain this answer) OPT 2'

        collideAnswer3 = opt3.collidepoint(point)
        if collideAnswer3:
            text = 'HMM, Possibly (Explain this answer) OPT 3'
    else:
        object_coordinates = (200, 125, 30, 30)
    return text, color


def nextQuestion():
    global question_number, points, answer1, answer2, answer3, text, answer, number
    items = list(CONSTANTS.QUESTIONS.keys())
    answer1 = customDrawText(items[question_number][1], 600, 100)
    answer2 = customDrawText(items[question_number][2], 600, 200)
    answer3 = customDrawText(items[question_number][3], 600, 300)
    answer = int(list(CONSTANTS.QUESTIONS.values())[question_number])
    pygame.display.update()


def finalInteract(character_rectangle, keys_pressed):
    global question_number, points

    if question_number >= len(CONSTANTS.QUESTIONS):
        return "", ""
    collideAnswer1 = character_rectangle.colliderect(answer1_rect)
    collideAnswer2 = character_rectangle.colliderect(answer2_rect)
    collideAnswer3 = character_rectangle.colliderect(answer3_rect)

    if collideAnswer1:
        option = "Option A? Press Enter"
    elif collideAnswer2:
        option = "Option B? Press Enter"
    elif collideAnswer3:
        option = "Option C? Press Enter"
    else:
        option = "Get on the right answer!"

    if collideAnswer1 and keys_pressed[pygame.K_RETURN]:
        if answer == 1:
            points += 1
            text = "Correct! +1 Point"
        else:
            text = "Incorrect! Next question!"
        question_number += 1
    elif collideAnswer2 and keys_pressed[pygame.K_RETURN]:
        if answer == 2:
            points += 1
            text = "Correct! +1 Point"
        else:
            text = "Incorrect! Next question!"
        question_number += 1
    elif collideAnswer3 and keys_pressed[pygame.K_RETURN]:
        if answer == 3:
            points += 1
            text = "Correct! +1 Point"
        else:
            text = "Incorrect! Next question!"
        question_number += 1
    else:
        text = list(CONSTANTS.QUESTIONS.keys())[question_number][0]
    return text, option
