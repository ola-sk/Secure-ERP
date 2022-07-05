import pygame
import sys
# import builtins
# from random import random

from button import Button
from fonts import get_font

pygame.mixer.init()  # odwarzacz dzwieku
pygame.init()
SCREEN = pygame.display.set_mode((600, 600))  # nasze okno windows
pygame.display.set_caption("SECURE ERP SYSTEM")  # nazwa okna

BG = pygame.image.load("assets/Background.png")
SONG = pygame.mixer.Sound('audio/menusong.mp3')
SONG.play()


def CRM_module():
    # CRM_menu()
    pass


def SALES_module():
    pass


def HR_module():
    pygame.quit()


def about():
    while True:
        ABOUT_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("gray")
        ABOUT_MENU_TEXT = get_font(50).render("CREADITS ERP SYSTEM ", True, "white")
        ABOUT_MENU_RECT = ABOUT_MENU_TEXT.get_rect(center=(320, 100))
        SCREEN.blit(ABOUT_MENU_TEXT, ABOUT_MENU_RECT)
        TEXT_PART = ["CREDITS:",
                     "",
                     "JULIA BUTKIEWICZ",
                     "",
                     "OLA SOKOLEK",
                     "",
                     "KRZYSZTOF KRÓL", ]
        pos_y = 200
        for line in range(len(TEXT_PART)):
            ABOUT_TEXT = get_font(40).render(TEXT_PART[line], True, "white")
            ABOUT_RECT = ABOUT_TEXT.get_rect(center=(320, pos_y))
            SCREEN.blit(ABOUT_TEXT, ABOUT_RECT)
            pos_y += 20

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
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(55).render("SECURE ERP", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(320, 50))

        CRM_BUTTON = Button(image=pygame.image.load("assets/crm_btn.png"), pos=(320, 140),
                            text_input="CRM MODULE", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        SALES_BUTTON = Button(image=pygame.image.load("assets/ssales_btn.png"), pos=(320, 240),
                              text_input="SALES MODULE", font=get_font(40), base_color="#d7fcd4",
                              hovering_color="White")
        HR_BUTTON = Button(image=pygame.image.load("assets/hhr_btn.png"), pos=(320, 340),
                           text_input="HR MODULE", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        ABOUT_BUTTON = Button(image=pygame.image.load("assets/about_btn.png"), pos=(320, 440),
                              text_input="ABOUT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/quit_btn.png"), pos=(320, 540),
                             text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [CRM_BUTTON, SALES_BUTTON, HR_BUTTON, ABOUT_BUTTON, QUIT_BUTTON, ]:
            button.change_color(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CRM_BUTTON.check_for_input(MENU_MOUSE_POS):
                    CRM_module()
                if SALES_BUTTON.check_for_input(MENU_MOUSE_POS):
                    SALES_module()
                if HR_BUTTON.check_for_input(MENU_MOUSE_POS):
                    HR_module()
                if ABOUT_BUTTON.check_for_input(MENU_MOUSE_POS):
                    about()
                if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

