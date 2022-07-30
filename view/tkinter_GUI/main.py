from tkinter import Tk
from view.tkinter_GUI.about_pages import *
from view.tkinter_GUI.menus import *
from view.tkinter_GUI.modules.crm import *
from view.tkinter_GUI.modules.hr import *
from view.tkinter_GUI.modules.sales import *


def initialise() -> Tk:
	"""Initialises graphical elements of User Interface. Creates an instance of a Tkinter application named `app` and
	sets its parameters, such as title, size of the window, icon. In this function also Images that are going to be used
	throughout the application, like a button image, are initialised to be available in the application."""
	app = Tk()
	app.title('Asparagusz - Secure Enterprise Resource Planning Software')
	app.geometry("1300x700")
	app.iconbitmap('./view/tkinter_GUI/assets/asparagusz.ico')
	return app


def finalise(app) -> None:
	app.mainloop()
	return None
