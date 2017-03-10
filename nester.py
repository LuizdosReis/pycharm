"""this is the 'nester.py' module and it provides one function called print_lol
wich prints lists that may or may not include nested lists"""

import sys


def print_lol(the_list, indent=False, level=0, file=sys.stdout):
    for item in the_list:
        if (isinstance(item, list)):
            if indent:
                level = level + 1
            print_lol(item, indent, level, file)
        else:
            for n in range(level):
                print('\t', end='', file=file);
            print(item, file=file);
