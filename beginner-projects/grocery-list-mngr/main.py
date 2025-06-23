# GROCERY LIST MANAGER (in memory; doesn't save)
# Add, remove, and sort grocery items (stored in a list of strings of tuples for (item, quantity)).
# Optionally store prices using a dictionary
import utils
from time import sleep

title = "GROCERY LIST MANAGER"

def menu(groceries):
    """ display the menu with options to choose from """
    while True:
        display_list_and_title(title, groceries)

        # user options
        print("1. Add items to the grocery list")
        print("2. Remove items from the grocery list")
        print("3. Clear the entire grocery list")
        print("4. Sort the grocery list")
        print("Q. Exit")
        utils.hyphens()
        
        # get user choice
        choice = input("Choice: ")
        if choice == '1':
            return 'add'
        elif choice == '2':
            return 'remove'
        elif choice == '3':
            return 'clear'
        elif choice == '4':
            return 'sort'
        elif choice.lower() == 'q':
            utils.clear_screen()
            print("Exiting...")
            sleep(0.75)
            utils.clear_screen()
            quit()
        else:
            continue

def display_list_and_title(title, groceries):
    """ for printing the title and the list within other functions """
    utils.display(title)
    display_list(groceries)
    utils.hyphens()

def parse_choice(menu_exit_code, groceries):
    """ get the exit code from menu() and then decide which function to execute """
    if menu_exit_code == 'add':
        add_menu(groceries)
    elif menu_exit_code == 'remove':
        if len(groceries) == 0:
            utils.clear_screen()
            print("The list is already empty.")
            sleep(1.5)
        else:
            remove_menu(groceries)
    elif menu_exit_code == 'clear':
        clear_list(groceries)
    elif menu_exit_code == 'sort':
        sort_list(groceries)

def add_menu(groceries):
    """ the menu for adding items to the grocery list """
    while True:
        display_list_and_title(title, groceries) # display title and groceries
        
        # add items to the list
        print("Enter 'Q' when you are finished")
        item_name = input("Add to list: ")
        if item_name.lower() == 'q':
            break
        else:
            while True:
                try:
                    display_list_and_title(title, groceries)
                    print(f"Add to list: {item_name.capitalize()}")

                    quantity = int(input("Quantity: ")) # let the user add a quantity
                    item = (item_name.capitalize(), quantity) # make it a tuple of (item, qnty)
                    groceries.append(item)
                    break
                except ValueError: # except value error in case the user enters a non-number
                    continue

def remove_menu(groceries):
    """ the menu for removing items from the grocery list """
    while True:
        display_list_and_title(title, groceries) # display title and groceries

        # remove items from the list
        print("Enter 'Q' when you are finished")
        item_index = input("Item to remove from list (index): ")
        if item_index.lower() == 'q':
            break
        elif item_index.lower() != 'q':
            try:
                del groceries[int(item_index) - 1]
            except IndexError: # catch index error so the program doesn't crash
                continue
            if len(groceries) == 0:
                utils.clear_screen()
                print("The list is now empty. Going back to the menu...")
                sleep(1.5)
                break

def clear_list(groceries):
    """ clear the grocery list """
    if len(groceries) == 0:
        utils.clear_screen()
        print("The list is already empty.") # exit and do nothing if list is empty
        sleep(1.5)
    else:
        utils.clear_screen()
        print("Clearing grocery list...")
        sleep(1.5)
        groceries.clear()

def display_list(groceries):
    """ display the grocery list """
    if len(groceries) == 0:
        utils.clear_screen()
        print("Grocery list is currently empty") # exit and do nothing if list is empty
    else:
        print("#\tName\t\tQuantity")
        print()
        for index, item in enumerate(groceries):
            print(f"{index + 1}.\t{item[0]}\t\t{item[1]}") # output each item in the list line by line

def sort_list(groceries):
    """ sorts the list in alphabetical order """
    if len(groceries) == 0:
        utils.clear_screen()
        print("The list is already empty.") # exit and do nothing if list is empty
        sleep(1.5)
    else:
        utils.clear_screen()
        groceries.sort()
        print("List sorted.")
        sleep(1.5)

def main():
    groceries = [] # initialize groceries list
    while True:
        menu_exit_code = menu(groceries) # get initial user choice
        parse_choice(menu_exit_code, groceries) # do one of the 4 possible functions on the list

if __name__ == '__main__':
    main()

