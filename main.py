import pygame
import os

WIDTH, HEIGHT = 1280, 720 #setting the resolution
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fixit") #the caption that appears at the top of the window

FPS = 60 #FPS of our game
VELOCITY = 5 #velocity of the character

GREEN = (0, 229, 0) #the background color

CHARACTER_RIGHT = pygame.image.load(os.path.join("Assets", "guy.webp.png"))#the model of the character
CHARACTER_LEFT = pygame.image.load(os.path.join("Assets", "guy.webp"))#the model of the character
CHARACTER_RIGHT = pygame.transform.scale(CHARACTER_RIGHT, (57, 100))
CHARACTER = CHARACTER_RIGHT

TEST_CHAR = pygame.image.load(os.path.join("Assets", "pixil-frame-0.png"))
def refresh(position, model):
    WINDOW.fill(GREEN)
    WINDOW.blit(model, (position.x, position.y))
    WINDOW.blit(TEST_CHAR, (500, 500))
    pygame.display.update()

def main(): #main function (main loop) of out game
    global CHARACTER
    character = pygame.Rect(0, 0, 115, 220)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        key = False
        if keys_pressed[pygame.K_UP] and character.y >= 0:
            character.y -= VELOCITY
        if keys_pressed[pygame.K_DOWN] and character.y <= 720-220:
            character.y += VELOCITY
        if keys_pressed[pygame.K_RIGHT] and character.x <= 1280-115:
            character.x += VELOCITY
            CHARACTER = CHARACTER_RIGHT
        if keys_pressed[pygame.K_LEFT] and character.x >= 0:
            character.x -= VELOCITY
            CHARACTER = CHARACTER_LEFT


        refresh(character, CHARACTER)

    pygame.quit()

if __name__ == "__main__": #checking that function called in the original file
    main()
