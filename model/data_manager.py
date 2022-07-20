def read_table_from_file(file_path: str, separator: str = ';') -> list:
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
                rows_and_columns.append(line.replace("\n", "").split(separator))
            return rows_and_columns
    except IOError:
        return None


def write_table_to_file(file_name, table, separator=';'):
    """Write tabular data into a CSV file.

    Args:
        file_name: The name of the file to write to.
        table: list of lists containing tabular data.
        separator: The CSV separator character
    """
    with open(file_name, "w") as file:
        for record in table:
            row = separator.join(record)
            file.write(row + "\n")
