from view import terminal as view


def validate_input(an_input: str, options: list) -> bool:
	try:
		if isinstance(an_input, str) and isinstance(options, list or tuple):
			for option in options:
				if an_input.lower() == option:
					return True
			return False
		else:
			raise TypeError("Wrong argument type/s for input validation.")
	except TypeError as error:
		view.print_error_message(str(error))
		return False


def filter_column_condition(table: list, column_index: int, content_is: str) -> list or None:
	filtered_table = []
	try:
		for row in table:
			for index, column in enumerate(row):
				if index == column_index and content_is == column:
					filtered_table.append(row)
		return filtered_table
	except (ValueError, TypeError) as error:
		view.print_error_message(str(error))
		return None


def is_number_of_fields_valid(data_record: list, table_headers: list) -> bool:
	if len(data_record) == len(table_headers):
		return True
	else:
		return False
