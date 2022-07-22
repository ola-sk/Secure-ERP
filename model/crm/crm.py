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
ALTERNATIVES = {"yes": ["yes", "tak", "y", "1"], "no": ["no", "nie", "n", "0"]}


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


def get_customer_ids(customer_table_headerless: list, id_column_index: int = 0) -> list or None:
	"""

	Args:
		customer_table_headerless: list of lists
		id_column_index: int - index of the column storing customer id.

	Returns:
		customer_id_column: list - list of customer ids.
		None: if a TypeError occurs
	"""
	try:
		if customer_table_headerless is None:
			raise TypeError
		customer_id_column = util.get_column_data(customer_table_headerless, id_column_index)
		return customer_id_column
	except TypeError:
		return None


def insert_customer_data(record: list, path: str = CUSTOMER_DATAFILE, separator: str = ";") -> bool:
	if data_manager.add_record_to_file(path, record, separator):
		is_success = True
		return is_success
	else:
		is_success = False
		return is_success


def get_customer_emails(customer_table_headerless: list, email_column_index: int = 2) -> list or None:
	try:
		if customer_table_headerless is None:
			raise TypeError
		customer_email_column = util.get_column_data(customer_table_headerless, email_column_index)
		return customer_email_column
	except TypeError:
		return None
