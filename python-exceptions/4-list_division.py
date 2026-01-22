#!/usr/bin/python3
"""List division function."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element 2 lists.

    Args:
        my_list_1: First list
        my_list_2: Second list
        list_length: Number of elements to process

    Returns:
        New list with division results (0 for errors)
    """
    new = []

    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            new.append(res)

    return new
