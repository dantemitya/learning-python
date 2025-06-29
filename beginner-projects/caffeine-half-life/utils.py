# USEFUL METHODS THAT CAN BE REUSED IN VARIOUS SCRIPTS

def clear_screen(length=100):
    """ clears the console screen using new lines. default length is 100 """
    print("\n"*length)

def hyphens(length=55):
    """ prints a line of hyphens for formatting. default length is 40 """
    print("-"*length)

def display(title):
    """ displays the title of the program 'nicely' """
    clear_screen()
    print(title.upper())
    hyphens()
