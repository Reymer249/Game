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

#character
CHARACTER = pygame.image.load(os.path.join("Assets", "guy.webp.png"))#the model of the character
