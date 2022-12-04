import pygame
import CONSTANTS


def movement(VELOCITY, character_rectangle, keys_pressed):
    if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]) and character_rectangle.y >= 0:
        character_rectangle.y -= VELOCITY
    if (keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]) and character_rectangle.y <= CONSTANTS.HEIGHT - CONSTANTS.SCALE_HEIGHT:
        character_rectangle.y += VELOCITY
    if (keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]) and character_rectangle.x <= CONSTANTS.WIDTH - CONSTANTS.SCALE_WIDTH:
        character_rectangle.x += VELOCITY
    if (keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]) and character_rectangle.x >= 0:
        character_rectangle.x -= VELOCITY

    return character_rectangle.x, character_rectangle.y


def turn(character, keys_pressed):
    if True not in keys_pressed:
        return CONSTANTS.CHARACTER_FRONT
    if (keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]):
        CONSTANTS.CHARACTER_RIGHT += 1
        if CONSTANTS.CHARACTER_RIGHT < CONSTANTS.PACE:
            return CONSTANTS.CHARACTER_RIGHT_WALK
        elif CONSTANTS.CHARACTER_RIGHT < 2*CONSTANTS.PACE:
            return CONSTANTS.CHARACTER_RIGHT_STAY
        else:
            CONSTANTS.CHARACTER_RIGHT = 0
            return CONSTANTS.CHARACTER_RIGHT_WALK
    if (keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]):
        CONSTANTS.CHARACTER_LEFT += 1
        if CONSTANTS.CHARACTER_LEFT < CONSTANTS.PACE:
            return CONSTANTS.CHARACTER_LEFT_WALK
        elif CONSTANTS.CHARACTER_LEFT < 2*CONSTANTS.PACE:
            return CONSTANTS.CHARACTER_LEFT_STAY
        else:
            CONSTANTS.CHARACTER_LEFT = 0
            return CONSTANTS.CHARACTER_LEFT_WALK
    if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]):
        CONSTANTS.CHARACTER_UP += 1
        if CONSTANTS.CHARACTER_UP < CONSTANTS.PACE:
            return CONSTANTS.CHARACTER_BACK_LEFT
        elif CONSTANTS.CHARACTER_UP < 2*CONSTANTS.PACE:
            return CONSTANTS.CHARACTER_BACK_RIGHT
        else:
            CONSTANTS.CHARACTER_UP = 0
            return CONSTANTS.CHARACTER_BACK_LEFT
    if (keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]):
        CONSTANTS.CHARACTER_DOWN += 1
        if CONSTANTS.CHARACTER_DOWN < CONSTANTS.PACE:
            return CONSTANTS.CHARACTER_FRONT_LEFT
        elif CONSTANTS.CHARACTER_DOWN < 2*CONSTANTS.PACE:
            return CONSTANTS.CHARACTER_FRONT_RIGHT
        else:
            CONSTANTS.CHARACTER_DOWN = 0
            return CONSTANTS.CHARACTER_FRONT_LEFT

    return CONSTANTS.CHARACTER_FRONT
