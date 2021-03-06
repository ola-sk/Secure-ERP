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


def generate_new_customer_id(customer_table_headerless: list, id_parameters: list = [4, 2, 2, 2]):
	customer_ids_taken = get_customer_ids(customer_table_headerless)
	if customer_ids_taken is None:
		raise ValueError(
			"Couldn't fetch customer ids. This step is necessary to generate a unique ID for a new customer.")
	new_customer_id = util.generate_unique_id(customer_ids_taken, *id_parameters)
	return new_customer_id


def insert_customer_data(new_customer_data: list, path: str = CUSTOMER_DATAFILE, separator: str = ";") -> bool:
	if data_manager.add_record_to_file(path, new_customer_data, separator):
		is_success = True
	else:
		is_success = False
	return is_success


def get_client_emails(customer_table_headerless: list):
	try:
		if customer_table_headerless is None:
			raise TypeError
		email_list = util.get_column_data(customer_table_headerless, CUSTOMER_TABLE_INDEXES["email"])
		return email_list
	except TypeError:
		return None
