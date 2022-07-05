import pygame
import sys
# import builtins
# from random import random

from button import Button
from fonts import get_font
from main_menu import main_menu

pygame.mixer.init()
pygame.init()
SCREEN = pygame.display.set_mode((600, 600))
pygame.display.set_caption("SALES MODULE MENU")

BG = pygame.image.load("assets/Background.png")


def name1():
    pass


def name2():
    pass


def name3():
    pass


def name4():
    pass


def SALES_MENU():
    while True:
        ABOUT_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("gray")
        ABOUT_MENU_TEXT = get_font(50).render("CRM MENU ", True, "white")
        ABOUT_MENU_RECT = ABOUT_MENU_TEXT.get_rect(center=(320, 100))
        SCREEN.blit(ABOUT_MENU_TEXT, ABOUT_MENU_RECT)
        ABOUT_BACK = Button(image=None, pos=(320, 520),
                            text_input="BACK", font=get_font(30), base_color="black", hovering_color="white")
        ABOUT_BACK.change_color(ABOUT_MOUSE_POS)
        ABOUT_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ABOUT_BACK.check_for_input(ABOUT_MOUSE_POS):
                    # was import main_menu from which the main menu was called after declaration. That is not a
                    # good practice because calls of functions are hidden or not clear.
                    # TODO instead either import main_menu in this file and call the function main_menu() here.
                    #  import both main_menu and sales_module to the controller and make controller
                    #  call main_menu if the flow gets to this point.
                    main_menu()
        pygame.display.update()
