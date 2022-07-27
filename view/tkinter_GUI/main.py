from tkinter import Tk
from view.tkinter_GUI.about_pages import *
from view.tkinter_GUI.menus import *
from view.tkinter_GUI.modules.crm import *
from view.tkinter_GUI.modules.hr import *
from view.tkinter_GUI.modules.sales import *


def initialise() -> Tk:
	app = Tk()
	app.title('Asparagusz - Secure Enterprise Resource Planning Software')
	app.geometry("1300x700")
	app.iconbitmap('./view/tkinter_GUI/assets/asparagusz.ico')
	return app


def finalise(app) -> None:
	app.mainloop()
	return None
