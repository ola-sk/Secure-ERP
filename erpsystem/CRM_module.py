import pygame
import sys
# import builtins
# from random import random

from button import Button
from fonts import get_font

SCREEN = pygame.display.set_mode((600, 600))
BG = pygame.image.load("assets/Background.png") 
def get_font(size): # ładowanie naszej czcionki tutaj quicksand
    return pygame.font.Font("assets/font1.otf", size) 

def CRM_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(55).render("CRM MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(320, 50))

        CRM_BUTTON = Button(image=pygame.image.load("assets/crm_btn.png"), pos=(320, 140), 
                            text_input="CRM MODULE", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        SALES_BUTTON = Button(image=pygame.image.load("assets/ssales_btn.png"), pos=(320, 240),
                            text_input="SALES MODULE", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        HR_BUTTON = Button(image=pygame.image.load("assets/hhr_btn.png"), pos=(320, 340),
                                text_input="HR MODULE", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        ABOUT_BUTTON = Button(image=pygame.image.load("assets/about_btn.png"), pos=(320, 440),
                            text_input="ABOUT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/quit_btn.png"), pos=(320, 540),
                            text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [CRM_BUTTON, SALES_BUTTON,HR_BUTTON, ABOUT_BUTTON, QUIT_BUTTON, ]:
            button.change_color(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CRM_BUTTON.check_for_input(MENU_MOUSE_POS):
                    CRM_menu()
                if SALES_BUTTON.check_for_input(MENU_MOUSE_POS):
                    CRM_menu()
                if HR_BUTTON.check_for_input(MENU_MOUSE_POS):
                   CRM_menu()
                if ABOUT_BUTTON.check_for_input(MENU_MOUSE_POS):
                    CRM_menu()
                if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
 
pygame.display.update()
CRM_menu()
