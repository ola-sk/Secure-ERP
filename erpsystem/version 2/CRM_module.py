import tkinter as tk


root = tk.Tk()
root.title("CRM Module")
root.geometry("450x200")


def retrievedata():
	''' get data stored '''
	global list_data
	list_data = []
	try:
		with open("../../../../../../../../../../../Downloads/save.txt", "r", encoding="utf-8") as file:
			for f in file:
				listbox.insert(tk.END, f.strip())
				list_data.append(f.strip())
				print(list_data)
	except:
		pass


def reload_data():
	listbox.delete(0, tk.END)
	for d in list_data:
		listbox.insert(0, d)


def add_user(event=1):
	global list_data
	if content1.get() != "":
		listbox.insert(tk.END, content1.get())
		list_data.append(content1.get())
		content1.set("")


def add_mail(event=1):
	global list_data
	if content2.get() != "":
		listbox.insert(tk.END, content2.get())
		list_data.append(content2.get())
		content2.set("")


def delete():
	global list_data
	listbox.delete(0, tk.END)
	list_data = []


def delete_selected():
	try:
		selected = listbox.get(listbox.curselection())
		listbox.delete(listbox.curselection())
		list_data.pop(list_data.index(selected))
		reload_data()
		listbox.selection_clear(0, tk.END)
		listbox.selection_set(0)
		listbox.activate(0)
		listbox.event_generate("&lt;&lt;ListboxSelect>>")
		print(listbox.curselection())
	except:
		pass


def quit():
	global root
	with open("../../../../../../../../../../../Downloads/save.txt", "w", encoding="utf-8") as file:
		for d in list_data:
			file.write(d + "\n")
	root.destroy()


# LISTBOX
name = tk.Label(text="Username:").place(x=20, y=0)
# surname = tk.Label(text = "Email:").place(x = 10, y = 20) 
content1 = tk.StringVar()
content2 = tk.StringVar()

entry1 = tk.Entry(root, textvariable=content1)
entry1.pack()

button_add_user = tk.Button(root, text="Add new customer", command=add_user).place(x=300, y=1)

button_add_mail = tk.Button(root, text="Add mail", command=add_mail, relief="flat").place(x=300, y=30)

button_delete = tk.Button(text="Remove all customers", command=delete, relief="groove").place(x=300, y=60)

button_delete_selected = tk.Button(text="Remove selected", command=delete_selected).place(x=300, y=90)

listbox = tk.Listbox(root)
listbox.pack()
entry1.bind("&lt;Return>", add_user)
# entry2.bind("&lt;Return>", add_user)
bquit = tk.Button(root, text="Quit and update", command=quit).place(x=300, y=120)

retrievedata()
root.mainloop()
