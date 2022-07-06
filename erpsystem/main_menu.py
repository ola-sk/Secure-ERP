import pygame, sys
from button import Button
import builtins
from fonts import get_font


pygame.mixer.init()  #odwarzacz dzwieku
pygame.init()
SCREEN = pygame.display.set_mode((600, 600))  #nasze okno windows
pygame.display.set_caption("SECURE ERP SYSTEM") #nazwa okna 
BG = pygame.image.load("erpsystem/assets/Background.png") 
SONG = pygame.mixer.Sound('erpsystem/audio/menusong.mp3')
# SONG.play()
 
def file_load(): #tymczasowo  pozniej wyrzuce do osobnego pliku
    file = open("erpsystem/game_stat.txt", "r")
    games = []
    for line in file:
        games.append(line.split("\t"))# "\t" sortuje listy ktore sa odzielone TAB
    return games

games=file_load()

def CRM_module():  
    while True:
        CRM_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("gray")
        CRM_MENU_TEXT = get_font(30).render("CRM MODULE ", True, "black")
        CRM_MENU_RECT = CRM_MENU_TEXT.get_rect(center=(320, 20))
        SCREEN.blit(CRM_MENU_TEXT, CRM_MENU_RECT)
        TEXT_PART = [" tu bedzie okienko "
        "i jednorożce"]
        pos_y = 200
        pos_x=320 
       
        for line in range(len(TEXT_PART)):
            CRM_TEXT = get_font(20).render(TEXT_PART[line], True, "black")
            CRM_RECT = CRM_TEXT.get_rect(center=(pos_x, pos_y))
            SCREEN.blit(CRM_TEXT, CRM_RECT)
            
        font_size=20    
        CRM_ADD = Button(image=None, pos=(200, 520),
                            text_input="ADD", font=get_font(font_size), base_color="blue", hovering_color="white")
        CRM_ADD.change_Color(CRM_MOUSE_POS)
        CRM_ADD.update(SCREEN)

        CRM_BACK = Button(image=None, pos=(300, 520),
                            text_input="BACK", font=get_font(font_size), base_color="black", hovering_color="white")
        CRM_BACK.change_Color(CRM_MOUSE_POS)
        CRM_BACK.update(SCREEN)

        CRM_DELETE = Button(image=None, pos=(400, 520),
                            text_input="DELETE", font=get_font(font_size), base_color="red", hovering_color="white")
        CRM_DELETE.change_Color(CRM_MOUSE_POS)
        CRM_DELETE.update(SCREEN)

        CRM_READLIST = Button(image=None, pos=(500, 520),
                            text_input="READLIST", font=get_font(font_size), base_color="red", hovering_color="white")
        CRM_READLIST.change_Color(CRM_MOUSE_POS)
        CRM_READLIST.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CRM_BACK.check_For_Input(CRM_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CRM_ADD.check_For_Input(CRM_MOUSE_POS):
                    main_menu() #do zmiany na wywylywana fukcje np dodawanie uzytkownik
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CRM_DELETE.check_For_Input(CRM_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CRM_READLIST.check_For_Input(CRM_MOUSE_POS):
                    pygame.Surface(list, (0,0))
                    
        pygame.display.update()
    
def SALES_module():
    pass
    
def HR_module():
    pass
    
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
        ABOUT_BACK.change_Color(ABOUT_MOUSE_POS)
        ABOUT_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ABOUT_BACK.check_For_Input(ABOUT_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(55).render("SECURE ERP", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(320, 50))

        CRM_BUTTON = Button(image=pygame.image.load("erpsystem/assets/crm_btn.png"), pos=(320, 140), 
                            text_input="CRM MODULE", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        SALES_BUTTON = Button(image=pygame.image.load("erpsystem/assets/ssales_btn.png"), pos=(320, 240),
                            text_input="SALES MODULE", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        HR_BUTTON = Button(image=pygame.image.load("erpsystem/assets/hhr_btn.png"), pos=(320, 340),
                                text_input="HR MODULE", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        ABOUT_BUTTON = Button(image=pygame.image.load("erpsystem/assets/about_btn.png"), pos=(320, 440),
                            text_input="ABOUT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("erpsystem/assets/quit_btn.png"), pos=(320, 540),
                            text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [CRM_BUTTON, SALES_BUTTON,HR_BUTTON, ABOUT_BUTTON, QUIT_BUTTON, ]:
            button.change_Color(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CRM_BUTTON.check_For_Input(MENU_MOUSE_POS):
                    CRM_module()
                if SALES_BUTTON.check_For_Input(MENU_MOUSE_POS):
                    SALES_module()
                if HR_BUTTON.check_For_Input(MENU_MOUSE_POS):
                    HR_module()
                if ABOUT_BUTTON.check_For_Input(MENU_MOUSE_POS):
                    about()
                if QUIT_BUTTON.check_For_Input(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()