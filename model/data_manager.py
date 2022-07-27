def read_table_from_file(file_path: str, separator: str = ';') -> list or None:
	"""Read CSV file into a data table.

	Args:
		file_path: The name of the CSV data file.
		separator: The CSV separator character

	Returns:
		The data parsed into a list of lists.
	"""
	try:
		rows_and_columns = []
		with open(file_path, "r") as file:
			lines = file.readlines()
			for line in lines:
				rows_and_columns.append(line.strip().split(separator))
			return rows_and_columns
	except IOError:
		return None


def add_record_to_file(file_path: str, record: list, separator: str = ";") -> bool:
	"""Appends a row of tabular data into a CSV file.

	Args:
		file_path: The name of the file to write to.
		record: list containing tabular data, representing a row of data.
		separator: The CSV separator character
	"""
	try:
		with open(file_path, "a") as file:
			row = separator.join(record)
			file.write("\n" + row)
		return True
	except IOError or ConnectionError or ValueError or TypeError:
		return False


def write_table_to_file(file_path: str, table: list, separator: str = ';') -> bool:
	"""Overwrite tabular data into a CSV file. If there is some data in the file, this function overwrites the data.

	Args:
		file_path: The name of the file to write to.
		table: list of lists containing tabular data.
		separator: The CSV separator character
	"""
	is_success = False
	with open(file_path, "w") as file:
		for record in table:
			row = separator.join(record)
			file.write(row + "\n")
			is_success = True
	return is_success
