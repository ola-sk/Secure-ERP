from turtle import update
from controller import helpers
from model.hr import hr
from view import terminal as view

from email import message


employees_list = []
def main_hr(message):
	while True:
		message = ("Welcome in HR_module. What would you like to do? ")
		if message == "P":
			print(employees_list)
		elif message == "D":
			delete_employee()
		elif message == "A":
			add_employee()
		elif message == "U":
			update_employee()
			return

def add_employee():
	view.print_error_message("Not implemented yet.")

def update_employee():
	view.print_error_message("Not implemented yet.")


def delete_employee():
	view.print_error_message("Not implemented yet.")


def get_oldest_and_youngest():
	view.print_error_message("Not implemented yet.")


# def get_average_age():
# 	view.print_error_message("Not implemented yet.")


# def next_birthdays():
# 	view.print_error_message("Not implemented yet.")


# def count_employees_with_clearance():
# 	view.print_error_message("Not implemented yet.")


# def count_employees_per_department():
# 	view.print_error_message("Not implemented yet.")


# def run_operation(option):
# 	if option == 1:
# 		main_hr()
# 	elif option == 2:
# 		add_employee()
# 	elif option == 3:
# 		update_employee()
# 	elif option == 4:
# 		delete_employee()
# 	elif option == 5:
# 		get_oldest_and_youngest()
# 	elif option == 6:
# 		get_average_age()
# 	elif option == 7:
# 		next_birthdays()
# 	elif option == 8:
# 		count_employees_with_clearance()
# 	elif option == 9:
# 		count_employees_per_department()
# 	elif option == 0:
# 		return
# 	else:
# 		raise KeyError("There is no such option.")


# def display_menu():
# 	options = [
# 		"Back to main menu",
# 		"List employees",
# 		"Add new employee",
# 		"Update employee",
# 		"Remove employee",
# 		"Oldest and youngest employees",
# 		"Employees average age",
# 		"Employees with birthdays in the next two weeks",
# 		"Employees with clearance level",
# 		"Employee numbers by department"]
# 	view.print_menu("Human resources", options)


# def menu():
# 	operation = None
# 	while operation != '0':
# 		display_menu()
# 		try:
# 			operation = view.get_input("Select an operation")
# 			run_operation(int(operation))
# 			helpers.get_user_acknowledgement("<< Press Enter >>")
# 		except KeyError as error:
# 			view.print_error_message(str(error))
