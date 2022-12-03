import random
import time
from datetime import datetime

import CONSTANTS
from CONSTANTS import *
import core.interact_logic as il


def refresh(aimbox, model, text, color, keys_pressed):
    # background and character
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(model, (aimbox.x, aimbox.y))

    # objects
    il.drawObject(color)
    il.drawText(text)
    il.interact(aimbox, keys_pressed)

    pygame.display.update()

def refreshFinal(aimbox, model, text, option, keys_pressed):
    # background and character
    WINDOW.blit(FINAL_BACKGROUND, (0, 0))
    WINDOW.blit(model, (aimbox.x, aimbox.y))

    new_round = text == "Correct! +1 Point" or text == "Incorrect! Next question!"
    end = il.question_number >= len(CONSTANTS.QUESTIONS)

    if end:
        var = 0
    elif new_round:
        WINDOW.blit(CONSTANTS.BOSS_WOOSH, (800, 400))
    else:
        if datetime.now().microsecond.real > 500000:
            WINDOW.blit(CONSTANTS.BOSS_RIGHT, (800, 400))
        else:
            WINDOW.blit(CONSTANTS.BOSS_LEFT, (800, 400))

    if end:
        if il.points >= len(list(CONSTANTS.QUESTIONS.keys())) / 2:
            il.drawText(f"YOU WON WITH {il.points} POINTS!")
        else:
            il.drawText(f"YOU LOST WITH {il.points} POINTS!")
    else:
        il.drawText(text)
        il.customDrawText(option, 600, 600)
        il.nextQuestion()
        il.interact(aimbox, keys_pressed)

    pygame.display.update()

    if new_round:
        il.number += 1
        time.sleep(3)



def refresh_main(start_rectangle, read_rectangle, exit_rectangle):
    WINDOW.fill(SOFT_BLUE)

    WINDOW.blit(START_BUTTON, (start_rectangle.x, start_rectangle.y))
    WINDOW.blit(READ_BUTTON, (read_rectangle.x, read_rectangle.y))
    WINDOW.blit(EXIT_BUTTON, (exit_rectangle.x, exit_rectangle.y))

    pygame.display.update()
