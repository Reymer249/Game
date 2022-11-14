import pygame
from CONSTANTS import *
def movement(VELOCITY, character_rectangle):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and character_rectangle.y >= 0:
        character_rectangle.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and character_rectangle.y <= 720-220:
        character_rectangle.y += VELOCITY
    if keys_pressed[pygame.K_RIGHT] and character_rectangle.x <= 1280-115:
        character_rectangle.x += VELOCITY
    if keys_pressed[pygame.K_LEFT] and character_rectangle.x >= 0:
        character_rectangle.x -= VELOCITY

    return character_rectangle.x, character_rectangle.y

def turn(character):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT]:
        return CHARACTER_RIGHT_1
    if keys_pressed[pygame.K_LEFT]:
        return CHARACTER_LEFT_1
    return character
