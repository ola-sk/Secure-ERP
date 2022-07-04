import pygame, sys
from button import Button
import builtins
from random import random

pygame.mixer.init()  
pygame.init()
SCREEN = pygame.display.set_mode((600, 600))  
pygame.display.set_caption("HR MODULE MENU") 

BG = pygame.image.load("assets/Background.png") 

def name1():
    pass
 
def name2():
    pass
    
def name3():
    pass
    

def name4():
    pass

def HR_MENU():
    while True:
        ABOUT_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("gray")
        ABOUT_MENU_TEXT = get_font(50).render("CRM MENU ", True, "white")
        ABOUT_MENU_RECT = ABOUT_MENU_TEXT.get_rect(center=(320, 100))
        SCREEN.blit(ABOUT_MENU_TEXT, ABOUT_MENU_RECT)
        ABOUT_BACK = Button(image=None, pos=(320, 520),
        text_input="BACK", font=get_font(30), base_color="black", hovering_color="white")
        ABOUT_BACK.changeColor(ABOUT_MOUSE_POS)
        ABOUT_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ABOUT_BACK.checkForInput(ABOUT_MOUSE_POS):
                    import main_menu
                    

        pygame.display.update()

HR_MENU()
