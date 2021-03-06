# controller/main_controller.py is called from the root of repo inside the erp.py, therefore it has access to folders
# like "view", "model", "controller" directly using just "from `directory_name` import `python_file_name`" import.
from tkinter import Tk

from controller import crm_controller, sales_controller, hr_controller

from view import terminal as view
# from view.tkinter_GUI import main as view


def run_the_app() -> None:
	app: Tk or None = view.initialise()
	# TODO: instead displaying `about ERP` display the log-in form upon successful log-in show main menu
	main_menu(app)
	view.finalise(app)

	return None


def load_module(option) -> None:
	if option == 1:
		crm_controller.menu()
	elif option == 2:
		sales_controller.menu()
	elif option == 3:
		hr_controller.menu()
	elif option == 0:
		return
	else:
		raise KeyError()


def display_menu() -> None:
	options = [
		"Exit program",
		"Customer Relationship Management (CRM)",
		"Sales",
		"Human Resources"]
	view.print_menu("Main menu", options)


menu_options_and_commands = {
		"Exit program": None,
		"Customer Relationship Management": crm_controller.menu,
		"Sales": sales_controller.menu,
		"Human Resources": hr_controller.menu
}


def handle_module_loading(option) -> None:
	try:
		load_module(int(option))
	except KeyError:
		view.print_error_message("There is no such option!")
	except ValueError:
		view.print_error_message("An integer was expected.")


def main_menu(app) -> None:
	try:
		if isinstance(app, Tk):
			view.display_menu(app, "Main menu", menu_options_and_commands)
		elif app is None:
			option = None
			while option != '0':
				display_menu()
				option = view.get_input("Select module")
				handle_module_loading(option)
			view.print_message("Good-bye!")
	except Exception as some_exception:
		view.print_error_message(some_exception)
