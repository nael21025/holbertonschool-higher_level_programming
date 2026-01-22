#!/usr/bin/python3
# Test script for python-exceptions

# Test 0: safe_print_list
def safe_print_list(my_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            printed += 1
        except IndexError:
            break
    print()
    return printed

my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))