from model.util import *
import random
import string


def test_shake():
    # a_list = [3, 7, 1, 4, 6, 2, 9, 0, 5, 8]
    # shaked_list = shake(a_list)
    # for item in a_list:
    #     assert item in shaked_list
    #
    for repetition in range(20):
        a_list = random.sample(string.digits, 10)
        shaked_list = shake(a_list)
        for item in a_list:
            assert item in shaked_list
