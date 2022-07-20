from model.crm.crm import CUSTOMER_DATAFILE, CUSTOMER_TABLE_HEADERS
from controller.crm_controller import *
from model.data_manager import read_table_from_file


def redirect_standard_output(callable):
    import io
    import sys

    captured_output = io.StringIO()
    sys.stdout = captured_output
    callable()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


def test_list_customers():
    # compare formatted table fed to the view.print_table() function with the standard output

    customers_data = read_table_from_file(DATAFILE)
    list_customers_print_out = redirect_standard_output(list_customers)
    for row in customers_data:
        for item in row:
            assert item in list_customers_print_out
