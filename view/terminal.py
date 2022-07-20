def print_menu(title: str, list_options: list) -> None:
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(title + ": ")
    for index, option in enumerate(list_options):
        if index == 0:
            continue
        else:
            print("(" + str(index) + ")", option)
    print("(0)", list_options[0])


def print_message(message: str) -> None:
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    from time import sleep
    print(message)
    sleep(3)


def get_minimum_column_width(a_list: list) -> int:
    longest_item_length = 0
    for item in a_list:
        if len(item) > longest_item_length:
            longest_item_length = len(item)
    return longest_item_length


def are_all_items_strings(a_list: list) -> bool:
    for item in a_list:
        if not isinstance(item, str):
            return False
    return True


def print_general_results(result: int or float or list or tuple or dict, label: str) -> None:
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    if isinstance(result, int):
        print(f"{label}: {result:.2f}")
    elif isinstance(result, float):
        print(f"{label}: {round(result, 2):.2f}")
    elif isinstance(result, list) or isinstance(result, tuple):  # handle lists or tuples
        from os import get_terminal_size
        if are_all_items_strings(result):
            print(label + ": ")
            column_width = get_minimum_column_width(result)
            number_of_columns = get_terminal_size().columns // (column_width + 2)
            for item in result:
                for column in range(number_of_columns):
                    print(f"{item:<{column_width}}; ")
                print("\n")
    elif isinstance(result, dict):
        # TODO implement printing dictionaries
        print_error_message("It is a dictionary. Printing of dictionaries is not yet implemented.")


def get_minimum_column_widths(table: list) -> list:
    min_column_widths = []
    number_of_columns = len(table[0])
    for column in range(number_of_columns):
        min_column_widths.append(0)
    for row in table:
        for index, column in enumerate(row):
            if min_column_widths[index] < len(column):
                min_column_widths[index] = len(column)
    return min_column_widths


def get_table_row_format(min_widths: list, separator: str, padding_size: int, padding_char=" ") -> str:
    from io import StringIO
    buffer = StringIO()
    buffer.write(separator)
    for width in min_widths:
        buffer.write(padding_size * padding_char)
        buffer.write("{:<")
        buffer.write(str(width))
        buffer.write("}")
        buffer.write(padding_size * padding_char)
        buffer.write(separator)
    table_row_format = buffer.getvalue()
    return table_row_format


def get_table_separator_length(min_widths, separator, padding_size):
    number_of_columns = len(min_widths)
    table_structure_width = len(separator) + (2 * number_of_columns * padding_size) + (number_of_columns * len(separator
                                                                                                               ))
    table_width = table_structure_width + sum(min_widths)
    return table_width


def format_table(table, is_headers=True) -> str:
    """Formats tabular data as follows:

    .--------------------------------.
    | ID     | PRODUCT    | TYPE     |
    |========|============|==========|
    |   0    |  Bazooka   | portable |
    |   1    | Sidewinder | missile  |
    '--------------------------------'

    Args:
        table: list of lists
            the table to print out.
        is_headers: boolean, default: True
            tells if the table provided has a header or not in the first row.

    Returns:
        table_in_string: str
            String representation of the formatted table.
    """
    from io import StringIO
    buffer = StringIO()

    min_widths = get_minimum_column_widths(table)
    padding_size = 1
    separator = "|"
    table_row_format = get_table_row_format(min_widths, separator, padding_size)
    horizontal_separator_length = get_table_separator_length(min_widths, separator, padding_size) - 2

    # separator top
    buffer.write(".")
    buffer.write("-" * horizontal_separator_length)
    buffer.write(".")
    buffer.write("\n")

    # table
    headers = []
    headers_separators = [width * "=" for width in min_widths]
    headers_separator_row_format = get_table_row_format(min_widths, separator, padding_size, "=")
    headers_separators = headers_separator_row_format.format(*headers_separators)
    for row_index, row in enumerate(table):
        if is_headers and row_index == 0:
            for column_index, column in enumerate(row):
                headers.append(column.upper())
            buffer.write(table_row_format.format(*headers))
            buffer.write("\n")
            buffer.write(headers_separators)
            buffer.write("\n")
        else:
            buffer.write(table_row_format.format(*row))
            buffer.write("\n")

    # separator bottom
    buffer.write("'")
    buffer.write("-" * horizontal_separator_length)
    buffer.write("'")
    table_in_string = buffer.getvalue()
    return table_in_string


def print_table(table: list) -> None:
    printable_table = format_table(table)
    print(printable_table)


def get_input(label: str) -> str:
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    user_input = input(label + ": ")
    return user_input


def get_inputs(labels: list) -> list:
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    pass


def print_error_message(message: str) -> None:
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    from time import sleep
    print(message)
    sleep(3)
