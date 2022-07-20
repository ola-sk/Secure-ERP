from tkinter import *
from tkinter import messagebox  


root = Tk()
root.title('...::: SECURE ERP SYSTEM :::...')
root.geometry("400x400")
#welcome message 
messagebox.showinfo("...::: SECURE ERP SYSTEM :::...","Welcome to Secure ERP System!")  



def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def show_text():
   my_label = Label(root, text="tu pojawia sie tekst...").pack()

menubar = Menu(root)
CRM_menu = Menu(menubar, tearoff=0)
CRM_menu.add_command(label="Add new customer", command=show_text)
CRM_menu.add_command(label="Back to main menu", command=donothing)
CRM_menu.add_command(label="Remove customer", command=donothing)
CRM_menu.add_command(label="List customers", command=donothing)
CRM_menu.add_command(label="Update customer", command=donothing)
CRM_menu.add_command(label="Subscribed customer emails", command=donothing)

menubar.add_cascade(label="CRM MODULE", menu=CRM_menu)

SALES_menu = Menu(menubar, tearoff=0)
SALES_menu.add_command(label="List transactions", command=donothing)
SALES_menu.add_command(label="Back to main menu", command=donothing)
SALES_menu.add_command(label="Add new transaction", command=donothing)
SALES_menu.add_command(label="Remove transaction", command=donothing)
SALES_menu.add_command(label="Update transaction", command=donothing)
SALES_menu.add_command(label="Get the transaction that made the biggest revenue", command=donothing)
SALES_menu.add_command(label="Get the product that made the biggest revenue altogether", command=donothing)
menubar.add_cascade(label="SALES Module", menu=SALES_menu)


HR_menu = Menu(menubar, tearoff=0)
HR_menu.add_separator()

HR_menu.add_command(label="Add new employees", command=donothing)
HR_menu.add_command(label="Back to main menu", command=donothing)
HR_menu.add_command(label="Remove employee", command=donothing)
HR_menu.add_command(label="List employee", command=donothing)
HR_menu.add_command(label="Update employee", command=donothing)
HR_menu.add_command(label="Oldest and youngest employees", command=donothing)
HR_menu.add_command(label="Employees average age", command=donothing)
HR_menu.add_command(label="Employees with birthdays in the next two weeks", command=donothing)
HR_menu.add_command(label="Employees with clearance level", command=donothing)
HR_menu.add_command(label="Employee numbers by department", command=donothing)
menubar.add_cascade(label="HR Module", menu=HR_menu)

aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="About", menu=aboutmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

menubar.add_command(label="Quit!", command=root.quit)

root.config(menu=menubar)
root.mainloop()