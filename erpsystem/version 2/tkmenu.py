from tkinter import *
from tkinter import messagebox
import CRM_module


root = Tk()
root.title('...::: SECURE ERP SYSTEM :::...')
root.geometry("400x400")


# welcome message
# messagebox.showinfo("...::: SECURE ERP SYSTEM :::...","Welcome to Secure ERP System!")  

def file_load():
	file = open("t.txt", "r", encoding='utf-8')
	list_customers = []

	for line in file:
		list_customers.append(line.split())  # "\t" sortuje listy ktore sa odzielone TAB
	return list_customers


list_customers = file_load()


def donothing():
	filewin = Toplevel(root)
	button = Button(filewin, text="Do nothing button")
	button.pack()


def show_list():
	my_label = Label(root, text=list_customers).pack()


def add_user():
	def adds(root):
		name = str(root.get())
		surname = str(root.get())
		result = name + ' ' + surname
		return result

	name = Label(text="Name:").place(x=30, y=10)
	surname = Label(text="Surname:").place(x=23, y=40)
	result = Label(text="Result:").place(x=30, y=120)
	e1 = Entry().place(x=80, y=10)
	e2 = Entry().place(x=80, y=40)
	e3 = Entry().place(x=80, y=120)
	b1 = Button(root, text='Add', command=adds).place(x=70, y=70)
	b2 = Button(root, text='Cancel', command=show_list).place(x=120, y=70)
	root.mainloop()


menubar = Menu(root)

CRM_menu = Menu(menubar, tearoff=0)
CRM_menu.add_command(label="Add new customer", command=add_user)
CRM_menu.add_command(label="Remove customer", command=add_user)
CRM_menu.add_command(label="List customers", command=show_list)
CRM_menu.add_command(label="Update customer", command=donothing)
CRM_menu.add_command(label="Subscribed customer emails", command=donothing)

menubar.add_cascade(label="CRM MODULE", menu=CRM_menu)

SALES_menu = Menu(menubar, tearoff=0)

SALES_menu.add_command(label="List transactions", command=donothing)
SALES_menu.add_command(label="Add new transaction", command=donothing)
SALES_menu.add_command(label="Remove transaction", command=donothing)
SALES_menu.add_command(label="Update transaction", command=donothing)
SALES_menu.add_command(label="Get the transaction that made the biggest revenue", command=donothing)
SALES_menu.add_command(label="Get the product that made the biggest revenue altogether", command=donothing)

menubar.add_cascade(label="SALES Module", menu=SALES_menu)

HR_menu = Menu(menubar, tearoff=0)

HR_menu.add_separator()
HR_menu.add_command(label="Add new employees", command=donothing)
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
