""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


CUSTOMER_DATAFILE = "./model/crm/crm.csv"
CUSTOMER_TABLE_HEADERS = ["id", "name", "email", "subscribed"]
CUSTOMER_TABLE_INDEXES = {"id": 0, "name": 1, "email": 2, "subscribed": 3}
SUBSCRIPTION_STATUSES = {"subscribed": "1", "not subscribed": "0"}


def read_customer_data(path: str = CUSTOMER_DATAFILE, headers: list = None, separator: str = ";") -> list or None:
    """
    Reads customers data from a file and adds headers if `headers` argument is provided/ is not None.
    Args:
        path: str - a path to customer data file.
        headers: list - a list of column headers of the customer's d
        separator: str - a separator between data fields in the customers' data file.

    Returns:
        customer_table: list of lists - a list of records, each containing one customer's data. A record is a list
        containing fields or data cells. If an IOError occurred the `customer_table` is None.
    """
    customer_table = data_manager.read_table_from_file(path, separator)
    if customer_table is not None and headers is not None:
        customer_table.insert(0, headers)
    return customer_table
