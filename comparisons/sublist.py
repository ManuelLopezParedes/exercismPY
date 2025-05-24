SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if list_one in list_two:
        return SUBLIST
    if list_two in list_one:
        return SUPERLIST
    return UNEQUAL