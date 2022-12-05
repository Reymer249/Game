import pygame


def check_mouse(left_rect, right_rect, exit_rect):
    mouse_point = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if left_rect.collidepoint(mouse_point) and mouse_pressed[0] == 1:
        return "left"
    elif right_rect.collidepoint(mouse_point) and mouse_pressed[0] == 1:
        return "right"
    elif exit_rect.collidepoint(mouse_point) and mouse_pressed[0] == 1:
        return "exit"
    else:
        return "none"
