import pygame
import CONSTANTS
from main import *
from CONSTANTS import *
from core.movement_logic import *

pygame.init()


text_font = pygame.font.SysFont(None, 30)

#Coordinates and sizes
text_box_size = (10, 600, 500, 100)

simulator_rect = pygame.Rect(200, 125, 30, 30)

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

    if collideProblem and  keys_pressed[pygame.K_RETURN]:
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
