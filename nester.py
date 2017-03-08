"""this is the 'nester.py' module and it provides one function called print_lol
wich prints lists that may or may not include nested lists"""
def print_lol(the_list):
    for item in the_list:
        if(isinstance(item,list)):
            print_lol(item)
        else:
            print(item);