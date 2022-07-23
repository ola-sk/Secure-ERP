from tkinter import Tk


def initialise() -> Tk:
	app = Tk()
	app.title('Asparagusz - Secure Enterprise Resource Planning Software')
	app.geometry("1300x700")
	app.iconbitmap('./view/tkinter_GUI/assets/asparagusz.ico')
	return app


def finalise(app) -> None:
	app.mainloop()
