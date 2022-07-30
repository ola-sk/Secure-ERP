from tkinter import Tk, PhotoImage, LEFT, CENTER
from tkinter.ttk import Frame, Label, Button, Style
from view.tkinter_GUI.assets.button_image_initialiser import *
menu_button_image = None
menu_button_image_long = None


def display_menu(app: Tk, title: str, options_and_callables: dict):
	"""Creates a frame with a number of buttons - menu options provided as an argument in a list. Clicking a button
	causes a call of callback function with a parameter that is the index of a particular clicked button.
	"""
	global menu_button_image
	global menu_button_image_long
	if menu_button_image is None:
		menu_button_image = initialise_menu_button_image("normal")
	if menu_button_image_long is None:
		menu_button_image_long = initialise_menu_button_image("long")
	menu_frame = Frame(app)
	title = Label(
		menu_frame,
		text=title,
		font=("Helvetica", 20),
		foreground="grey",
		anchor="nw"
	).pack(ipadx=150, ipady=35)
	menu_button_style = Style(menu_frame)
	menu_button_style.configure("TButton", font=("Helvetica", 18), foreground="#26260a")
	for index, (option, command) in enumerate(options_and_callables.items()):
		if len(option) > 16:
			Button(
				menu_frame,
				image=menu_button_image_long,
				text=option,
				compound=CENTER,
				command=command
			).pack()
		else:
			Button(
				menu_frame,
				image=menu_button_image,
				text=option,
				compound=CENTER,
				command=command
			).pack()

	menu_frame.pack()

	# menu_frame.pack_forget()
	return
