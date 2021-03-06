from controller.crm_controller import *
from model import data_manager


def redirect_standard_output(a_callable):
	import io
	import sys

	captured_output = io.StringIO()
	sys.stdout = captured_output
	a_callable()
	sys.stdout = sys.__stdout__
	return captured_output.getvalue()


def test_list_customers():
	# compare formatted table fed to the view.print_table() function with the standard output

	customers_data = data_manager.read_table_from_file(CUSTOMER_DATAFILE)
	list_customers_print_out = redirect_standard_output(list_customers)
	for row in customers_data:
		for item in row:
			assert item in list_customers_print_out
