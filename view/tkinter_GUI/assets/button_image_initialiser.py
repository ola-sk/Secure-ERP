from tkinter import PhotoImage


def initialise_menu_button_image(flag: str):
	if flag == "normal":
		menu_button_image = PhotoImage(file="./view/tkinter_GUI/assets/button_image_v2.png")
	elif flag == "long":
		menu_button_image = PhotoImage(file="./view/tkinter_GUI/assets/button_image_v2_long.png")
	else:
		return None
	return menu_button_image
