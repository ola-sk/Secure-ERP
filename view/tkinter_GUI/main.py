from tkinter import *
from view.tkinter_GUI import about_pages

app = Tk()
app.title('Asparagusz - Secure Enterprise Resource Planning Software')
app.geometry("1300x700")
app.iconbitmap('./view/tkinter_GUI/assets/asparagusz.ico')
about_pages.display_about_enterprise_resource_planning(app)

app.mainloop()
