import pygame
import os

#window
WIDTH, HEIGHT = 1280, 720 #resolution
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) #applying resolution to the window
pygame.display.set_caption("Fixit") #the caption that appears at the top of the window

#game flow setting
FPS = 60 #FPS of our game
VELOCITY = 5 #velocity of the character

#background
GREEN = (0, 229, 0) #the background color

#character models
CHARACTER_RIGHT_1 = pygame.image.load(os.path.join("Assets", "guy.webp.png"))#right step 1
CHARACTER_LEFT_1 = pygame.image.load(os.path.join("Assets", "guy.webp"))#left step 1

CHARACTER = CHARACTER_RIGHT_1
