import pygame


def check_mouse(start_rectangle, read_rectangle, exit_rectangle):
    mouse_point = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if start_rectangle.collidepoint(mouse_point) and mouse_pressed[0] == 1:
        return "start"
    elif read_rectangle.collidepoint(mouse_point) and mouse_pressed[0] == 1:
        return "read"
    elif exit_rectangle.collidepoint(mouse_point) and mouse_pressed[0] == 1:
        return "exit"
    else:
        return "none"
