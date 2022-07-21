from tkinter.ttk import Label, Frame


def display_about_enterprise_resource_planning(app):
	about_enterprise_resource_planning_frame = Frame(app)
	title = Label(
		about_enterprise_resource_planning_frame,
		text="What is Enterprise Resource Planning?",
		font=("Georgia", 18),
		anchor="center"
	)
	main_citation = Label(
		about_enterprise_resource_planning_frame,
		text="\"Enterprise resource planning is the integrated management of main business processes, \n"
		"often in real time and mediated by software and technology.\" source: Wikipedia",
		font=("Georgia", 14),
		anchor="center"
	)
	text = Label(
		about_enterprise_resource_planning_frame,
		text="Each company is different. The bigger the company, \n"
		"the more diverse the needs might be.\n"
		"But all companies use data in some way to manage resources. \n"
		"In each of them a different kind of data is relevant. \n"
		"Among those there is accounting data, data about employees, \n"
		"products, stock, customers, income and expenditures.\n\n"
		"Having a secure and reliable system for managing this data \n"
		"is at the core of any company. \n"
		"Taking an example on customer relationship management: \n"
		"Without the clients' data, one may not be able to sell \n"
		"your product to those, who want to buy it.\n"
		"Without a system that lets the employee access relevant data \n"
		"about the client, the product and its warranty and the transaction, \n"
		"it is difficult to make the process of repair efficient \n"
		"without a technological solution that would enable the client to \n"
		"get a smooth communication experience.\n",
		font=("Georgia", 14),
		anchor="center"
	)
	title.pack(ipadx=150, ipady=35)
	main_citation.pack(ipadx=150, ipady=15)
	text.pack(ipadx=150, ipady=20)
	about_enterprise_resource_planning_frame.pack()
