import random
import string


def mix(a_list: list):
    index_order = random.sample(range(len(a_list)), len(a_list))
    mixed_list = []
    for index in index_order:
        mixed_list.append(a_list[index])
    return mixed_list


def swap(item_a, item_b):
    return item_b, item_a


def shake(a_list: list):
    for index, item in enumerate(a_list):
        if 1 <= index < (len(a_list) - 1):
            front_shake = random.choice([True, False])
            back_shake = random.choice([True, False])
            front_shake_goes_first = random.choice([True, False])
            if front_shake and front_shake_goes_first:
                item, a_list[index + 1] = swap(item, a_list[index + 1])
            if back_shake:
                item, a_list[index - 1] = swap(item, a_list[index - 1])
            if front_shake and not front_shake_goes_first:
                item, a_list[index + 1] = swap(item, a_list[index + 1])
    return a_list


def convert_list_to_string(a_list: list) -> str:
    """

    Args:
        a_list: list - list to be converted

    Returns:
        a_string: str - a string made of the list items joined together

    """
    a_string = "".join(a_list)
    return a_string


def generate_id(number_of_small_letters: int = 4,
                number_of_capital_letters: int = 2,
                number_of_digits: int = 2,
                number_of_special_chars: int = 2,
                allowed_special_chars=r"_+-!") -> str:
    id_characters = []
    id_characters.extend(random.choices(string.ascii_lowercase, k=number_of_small_letters))
    id_characters.extend(random.choices(string.ascii_uppercase, k=number_of_capital_letters))
    id_characters.extend(random.choices(string.digits, k=number_of_digits))
    id_characters.extend(random.choices(allowed_special_chars, k=number_of_special_chars))
    id_characters_mixed_shaken = mix(shake(id_characters))
    generated_id = convert_list_to_string(id_characters_mixed_shaken)
    return generated_id  # 'T!uq6-b4Yq'


def is_id_unique(the_id: str, collection: list) -> bool:
    if the_id in collection:
        return False
    return True


def generate_unique_id(collection: list,
                       number_of_small_letters=4,
                       number_of_capital_letters=2,
                       number_of_digits=2,
                       number_of_special_chars=2,
                       allowed_special_chars=r"_+-!") -> str:
    """
    Generate an ID that is unique in the `collection` of IDs.
    Args:
        collection (object): list - list of IDs
        number_of_small_letters: int - number of lowercase letters that the ID should contain
        number_of_capital_letters: int - number of capital letter that the ID should contain
        number_of_digits: int - number of digits that the ID should contain
        number_of_special_chars: int - number of special characters that the ID should contain
        allowed_special_chars: str - special characters that are allowed to be used in ID
    """
    new_id = generate_id(number_of_small_letters, number_of_capital_letters, number_of_digits, number_of_special_chars,
                         allowed_special_chars)
    if is_id_unique(new_id, collection):
        return new_id
    else:
        return generate_unique_id(collection, number_of_small_letters, number_of_capital_letters, number_of_digits,
                                  number_of_special_chars, allowed_special_chars)


def table_check_for_minimum_number_of_columns(table: list, minimum_number_of_columns: int) -> bool:
    for row in table:
        if (len(row) - 1) < minimum_number_of_columns:
            return False
        else:
            return True


def get_column_data(table: list = None, column_index: int = None) -> list or None:
    """
    Gets column items from a two-dimensional list. Returns a list of those items.
    Args:
        table: list of lists. A table with the first dimension being rows and the second - columns.
        column_index: Index of a column to be fetched from a table.

    Returns:
        column_data: list of all items from a column of index `column_index`
    """
    from view.terminal import print_error_message
    try:
        if isinstance(table, list) and isinstance(column_index, int):
            if column_index >= 0:
                if not table_check_for_minimum_number_of_columns(table, column_index):
                    raise KeyError("Warning when trying to fetch column data: Inconsistent table data. Result of the "
                                   "processing of an inconsistent data may yield invalid and/or malformed results.")
                column_data = []
                for row in table:
                    for index, column in enumerate(row):
                        if index == column_index:
                            column_data.append(column)
                return column_data
            else:
                raise ValueError("Error when trying to fetch column data. Column index out of range.")
        else:
            raise TypeError("Error when trying to fetch column data. Either table or index of an inappropriate type.")
    except (TypeError, ValueError, KeyError) as error:
        print_error_message(error)
        return None
