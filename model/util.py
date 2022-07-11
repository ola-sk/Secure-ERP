import random
import string


def mix(a_list):
    index_order = random.sample(range(len(a_list)), len(a_list))
    mixed_list = []
    for index in index_order:
        mixed_list.append(a_list[index])
    return mixed_list


def swap(item_a, item_b):
    return item_b, item_a


def shake(a_list):
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


def convert_list_to_string(a_list):
    a_string = "".join(a_list)
    return a_string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    id_characters = []
    id_characters.extend(random.choices(string.ascii_lowercase, k=number_of_small_letters))
    id_characters.extend(random.choices(string.ascii_uppercase, k=number_of_capital_letters))
    id_characters.extend(random.choices(string.digits, k=number_of_digits))
    id_characters.extend(random.choices(allowed_special_chars, k=number_of_special_chars))
    id_characters_mixed_shaked = mix(shake(id_characters))
    generated_id = convert_list_to_string(id_characters_mixed_shaked)
    return generated_id  # 'T!uq6-b4Yq'
