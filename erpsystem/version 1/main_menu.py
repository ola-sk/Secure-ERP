import pygame, sys
from button import Button
import builtins
from fonts import get_font
from tkinter import filedialog
import tkinter as tk


pygame.mixer.init()  # odwarzacz dzwieku
pygame.init()
SCREEN = pygame.display.set_mode((600, 600))  # nasze okno windows
pygame.display.set_caption("SECURE ERP SYSTEM")  # nazwa okna
BG = pygame.image.load("erpsystem/assets/Background.png")
SONG = pygame.mixer.Sound('erpsystem/audio/menusong.mp3')
# SONG.play()
# _________________________________________________________
# okienko wprowadzania w tkinter
input_box = tk.Tk()
input_box.geometry("150x210")


def getTextInput():
	result = textExample.get(1.0, tk.END + "-1c")
	print(result)  # test
	return result


textExample = tk.Text(input_box, height=10)
textExample.pack()
btnSave = tk.Button(input_box, height=1, width=10, text="SAVE",
					command=getTextInput)
btnSave.pack()


# _________________________________________________________


def file_load():  # tymczasowo  pozniej wyrzuce do osobnego pliku
	file = open("erpsystem/t.txt", "r", encoding='utf-8')
	games = []

	for line in file:
		games.append(line.split())  # "\t" sortuje listy ktore sa odzielone TAB


# return games


games = file_load()
print(games)


def CRM_module():
	while True:
		SCREEN.blit(BG, (0, 0))
		CRM_MOUSE_POS = pygame.mouse.get_pos()
		CRM_MENU_TEXT = get_font(20).render("CRM MODULE ", True, "black")
		CRM_MENU_RECT = CRM_MENU_TEXT.get_rect(center=(100, 20))
		SCREEN.blit(CRM_MENU_TEXT, CRM_MENU_RECT)

		TEXT_PART = ["moze sie uda tu wczytac liste"]

		pos_y = 200
		pos_x = 320

		for line in range(len(TEXT_PART)):
			CRM_TEXT = get_font(20).render(TEXT_PART[line], True, "black")
			CRM_RECT = CRM_TEXT.get_rect(center=(pos_x, pos_y))
			SCREEN.blit(CRM_TEXT, CRM_RECT)

		font_size = 15
		CRM_ADD_CUSTOMER = Button(image=None, pos=(100, 500),
								  text_input="Add new customer", font=get_font(font_size), base_color="blue",
								  hovering_color="white")
		CRM_ADD_CUSTOMER.change_Color(CRM_MOUSE_POS)
		CRM_ADD_CUSTOMER.update(SCREEN)

		CRM_BACK = Button(image=None, pos=(100, 580),
						  text_input="Back to main menu", font=get_font(font_size), base_color="black",
						  hovering_color="white")
		CRM_BACK.change_Color(CRM_MOUSE_POS)
		CRM_BACK.update(SCREEN)

		CRM_REMOVE_CUSTOMER = Button(image=None, pos=(300, 500),
									 text_input="Remove customer", font=get_font(font_size), base_color="red",
									 hovering_color="white")
		CRM_REMOVE_CUSTOMER.change_Color(CRM_MOUSE_POS)
		CRM_REMOVE_CUSTOMER.update(SCREEN)

		CRM_LIST_CUSTOMERS = Button(image=None, pos=(100, 520),
									text_input="List customers", font=get_font(font_size), base_color="red",
									hovering_color="white")
		CRM_LIST_CUSTOMERS.change_Color(CRM_MOUSE_POS)
		CRM_LIST_CUSTOMERS.update(SCREEN)

		CRM_UPDATE_CUSTOMER = Button(image=None, pos=(500, 500),
									 text_input="Update customer", font=get_font(font_size), base_color="red",
									 hovering_color="white")
		CRM_UPDATE_CUSTOMER.change_Color(CRM_MOUSE_POS)
		CRM_UPDATE_CUSTOMER.update(SCREEN)

		CRM_EMAIL = Button(image=None, pos=(350, 520),
						   text_input="Subscribed customer emails", font=get_font(font_size), base_color="red",
						   hovering_color="white")
		CRM_EMAIL.change_Color(CRM_MOUSE_POS)
		CRM_EMAIL.update(SCREEN)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if CRM_BACK.check_For_Input(CRM_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if CRM_ADD_CUSTOMER.check_For_Input(CRM_MOUSE_POS):
					input_box.mainloop()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if CRM_REMOVE_CUSTOMER.check_For_Input(CRM_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if CRM_LIST_CUSTOMERS.check_For_Input(CRM_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if CRM_UPDATE_CUSTOMER.check_For_Input(CRM_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if CRM_EMAIL.check_For_Input(CRM_MOUSE_POS):
					main_menu()
		pygame.display.update()


def SALES_module():
	while True:
		SCREEN.blit(BG, (0, 0))
		SALES_MOUSE_POS = pygame.mouse.get_pos()
		SALES_MENU_TEXT = get_font(20).render("SALES MODULE ", True, "black")
		SALES_MENU_RECT = SALES_MENU_TEXT.get_rect(center=(100, 20))
		SCREEN.blit(SALES_MENU_TEXT, SALES_MENU_RECT)
		TEXT_PART = [""]
		pos_y = 200
		pos_x = 320

		for line in range(len(TEXT_PART)):
			SALES_TEXT = get_font(20).render(TEXT_PART[line], True, "black")
			SALES_RECT = SALES_TEXT.get_rect(center=(pos_x, pos_y))
			SCREEN.blit(SALES_TEXT, SALES_RECT)

		font_size = 10
		SALES_LIST_TRANS = Button(image=None, pos=(400, 50),
								  text_input="List transactions", font=get_font(font_size), base_color="blue",
								  hovering_color="white")
		SALES_LIST_TRANS.change_Color(SALES_MOUSE_POS)
		SALES_LIST_TRANS.update(SCREEN)

		SALES_BACK = Button(image=None, pos=(100, 580),
							text_input="Back to main menu", font=get_font(font_size), base_color="black",
							hovering_color="white")
		SALES_BACK.change_Color(SALES_MOUSE_POS)
		SALES_BACK.update(SCREEN)

		SALES_ADD_NEW_TRANS = Button(image=None, pos=(400, 100),
									 text_input="Add new transaction", font=get_font(font_size), base_color="red",
									 hovering_color="white")
		SALES_ADD_NEW_TRANS.change_Color(SALES_MOUSE_POS)
		SALES_ADD_NEW_TRANS.update(SCREEN)

		SALES_REMOVE_TRANS = Button(image=None, pos=(400, 150),
									text_input="Remove transaction", font=get_font(font_size), base_color="red",
									hovering_color="white")
		SALES_REMOVE_TRANS.change_Color(SALES_MOUSE_POS)
		SALES_REMOVE_TRANS.update(SCREEN)

		SALES_UPDATE_TRANS = Button(image=None, pos=(400, 200),
									text_input="Update transaction", font=get_font(font_size), base_color="red",
									hovering_color="white")
		SALES_UPDATE_TRANS.change_Color(SALES_MOUSE_POS)
		SALES_UPDATE_TRANS.update(SCREEN)

		SALES_BIGGEST_REVENUE = Button(image=None, pos=(400, 250),
									   text_input="Get the transaction that made the biggest revenue",
									   font=get_font(font_size), base_color="red", hovering_color="white")
		SALES_BIGGEST_REVENUE.change_Color(SALES_MOUSE_POS)
		SALES_BIGGEST_REVENUE.update(SCREEN)

		SALES_PRODUCT_BIGGEST_REVENUE = Button(image=None, pos=(400, 300),
											   text_input="Get the product that made the biggest revenue altogether",
											   font=get_font(font_size), base_color="red", hovering_color="white")
		SALES_PRODUCT_BIGGEST_REVENUE.change_Color(SALES_MOUSE_POS)
		SALES_PRODUCT_BIGGEST_REVENUE.update(SCREEN)

		SALES_TRANSACTIONS_NUMER = Button(image=None, pos=(400, 350),
										  text_input="Count number of transactions between", font=get_font(font_size),
										  base_color="red", hovering_color="white")
		SALES_TRANSACTIONS_NUMER.change_Color(SALES_MOUSE_POS)
		SALES_TRANSACTIONS_NUMER.update(SCREEN)

		SALES_TRANSACTIONS_PRICE = Button(image=None, pos=(400, 400),
										  text_input="Sum the price of transactions between", font=get_font(font_size),
										  base_color="red", hovering_color="white")
		SALES_TRANSACTIONS_PRICE.change_Color(SALES_MOUSE_POS)
		SALES_TRANSACTIONS_PRICE.update(SCREEN)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if SALES_BACK.check_For_Input(SALES_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if SALES_LIST_TRANS.check_For_Input(SALES_MOUSE_POS):
					main_menu()  # do zmiany na wywylywana fukcje np dodawanie uzytkownik
			if event.type == pygame.MOUSEBUTTONDOWN:
				if SALES_ADD_NEW_TRANS.check_For_Input(SALES_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if SALES_REMOVE_TRANS.check_For_Input(SALES_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if SALES_UPDATE_TRANS.check_For_Input(SALES_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if SALES_BIGGEST_REVENUE.check_For_Input(SALES_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if SALES_PRODUCT_BIGGEST_REVENUE.check_For_Input(SALES_MOUSE_POS):
					main_menu()  # do zmiany na wywylywana fukcje np dodawanie uzytkownik
			if event.type == pygame.MOUSEBUTTONDOWN:
				if SALES_TRANSACTIONS_NUMER.check_For_Input(SALES_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if SALES_TRANSACTIONS_PRICE.check_For_Input(SALES_MOUSE_POS):
					main_menu()

		pygame.display.update()


def HR_module():
	while True:
		SCREEN.blit(BG, (0, 0))
		HR_MOUSE_POS = pygame.mouse.get_pos()
		HR_MENU_TEXT = get_font(20).render("HR MODULE ", True, "black")
		HR_MENU_RECT = HR_MENU_TEXT.get_rect(center=(100, 20))
		SCREEN.blit(HR_MENU_TEXT, HR_MENU_RECT)
		TEXT_PART = [" .... "
					 ""]
		pos_y = 200
		pos_x = 320

		for line in range(len(TEXT_PART)):
			HR_TEXT = get_font(20).render(TEXT_PART[line], True, "black")
			HR_RECT = HR_TEXT.get_rect(center=(pos_x, pos_y))
			SCREEN.blit(HR_TEXT, HR_RECT)

		font_size = 10
		HR_ADD_EMPLOYEE = Button(image=None, pos=(400, 50),
								 text_input="Add new employees", font=get_font(font_size), base_color="blue",
								 hovering_color="white")
		HR_ADD_EMPLOYEE.change_Color(HR_MOUSE_POS)
		HR_ADD_EMPLOYEE.update(SCREEN)

		HR_BACK = Button(image=None, pos=(100, 580),
						 text_input="Back to main menu", font=get_font(font_size), base_color="black",
						 hovering_color="white")
		HR_BACK.change_Color(HR_MOUSE_POS)
		HR_BACK.update(SCREEN)

		HR_REMOVE_EMPLOYEE = Button(image=None, pos=(400, 100),
									text_input="Remove employee", font=get_font(font_size), base_color="red",
									hovering_color="white")
		HR_REMOVE_EMPLOYEE.change_Color(HR_MOUSE_POS)
		HR_REMOVE_EMPLOYEE.update(SCREEN)

		HR_LIST_EMPLOYEE = Button(image=None, pos=(400, 150),
								  text_input="List employee", font=get_font(font_size), base_color="red",
								  hovering_color="white")
		HR_LIST_EMPLOYEE.change_Color(HR_MOUSE_POS)
		HR_LIST_EMPLOYEE.update(SCREEN)

		HR_UPDATE_EMPLOYEE = Button(image=None, pos=(400, 200),
									text_input="Update employee", font=get_font(font_size), base_color="red",
									hovering_color="white")
		HR_UPDATE_EMPLOYEE.change_Color(HR_MOUSE_POS)
		HR_UPDATE_EMPLOYEE.update(SCREEN)

		HR_OLD_TO_YOUNG = Button(image=None, pos=(400, 250),
								 text_input="Oldest and youngest employees", font=get_font(font_size), base_color="red",
								 hovering_color="white")
		HR_OLD_TO_YOUNG.change_Color(HR_MOUSE_POS)
		HR_OLD_TO_YOUNG.update(SCREEN)

		HR_AVERAGE_AGE = Button(image=None, pos=(400, 300),
								text_input="Employees average age", font=get_font(font_size), base_color="red",
								hovering_color="white")
		HR_AVERAGE_AGE.change_Color(HR_MOUSE_POS)
		HR_AVERAGE_AGE.update(SCREEN)

		HR_BIRTHDAY_NEXT_2WEEKS = Button(image=None, pos=(400, 350),
										 text_input="Employees with birthdays in the next two weeks",
										 font=get_font(font_size), base_color="red", hovering_color="white")
		HR_BIRTHDAY_NEXT_2WEEKS.change_Color(HR_MOUSE_POS)
		HR_BIRTHDAY_NEXT_2WEEKS.update(SCREEN)

		HR_CLEARANCE_LEVEL = Button(image=None, pos=(400, 400),
									text_input="Employees with clearance level", font=get_font(font_size),
									base_color="red", hovering_color="white")
		HR_CLEARANCE_LEVEL.change_Color(HR_MOUSE_POS)
		HR_CLEARANCE_LEVEL.update(SCREEN)

		HR_NUMBER_DEPARTMENT = Button(image=None, pos=(400, 450),
									  text_input="Employee numbers by department", font=get_font(font_size),
									  base_color="red", hovering_color="white")
		HR_NUMBER_DEPARTMENT.change_Color(HR_MOUSE_POS)
		HR_NUMBER_DEPARTMENT.update(SCREEN)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if HR_BACK.check_For_Input(HR_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if HR_ADD_EMPLOYEE.check_For_Input(HR_MOUSE_POS):
					main_menu()  # do zmiany na wywylywana fukcje np dodawanie uzytkownik
			if event.type == pygame.MOUSEBUTTONDOWN:
				if HR_REMOVE_EMPLOYEE.check_For_Input(HR_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if HR_LIST_EMPLOYEE.check_For_Input(HR_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if HR_UPDATE_EMPLOYEE.check_For_Input(HR_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if HR_OLD_TO_YOUNG.check_For_Input(HR_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if HR_AVERAGE_AGE.check_For_Input(HR_MOUSE_POS):
					main_menu()  # do zmiany na wywylywana fukcje np dodawanie uzytkownik
			if event.type == pygame.MOUSEBUTTONDOWN:
				if HR_BIRTHDAY_NEXT_2WEEKS.check_For_Input(HR_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if HR_CLEARANCE_LEVEL.check_For_Input(HR_MOUSE_POS):
					main_menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if HR_NUMBER_DEPARTMENT.check_For_Input(HR_MOUSE_POS):
					main_menu()

		pygame.display.update()


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
							  text_input="SALES MODULE", font=get_font(40), base_color="#d7fcd4",
							  hovering_color="White")
		HR_BUTTON = Button(image=pygame.image.load("erpsystem/assets/hhr_btn.png"), pos=(320, 340),
						   text_input="HR MODULE", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
		ABOUT_BUTTON = Button(image=pygame.image.load("erpsystem/assets/about_btn.png"), pos=(320, 440),
							  text_input="ABOUT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
		QUIT_BUTTON = Button(image=pygame.image.load("erpsystem/assets/quit_btn.png"), pos=(320, 540),
							 text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

		SCREEN.blit(MENU_TEXT, MENU_RECT)

		for button in [CRM_BUTTON, SALES_BUTTON, HR_BUTTON, ABOUT_BUTTON, QUIT_BUTTON, ]:
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


if __name__ == '__main__':
	main_menu()
