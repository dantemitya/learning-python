from time import sleep


def clear_screen(length=100):
    """ clears the console screen using new lines. default length is 100 """
    print("\n"*length)


def hyphens(length=40):
    """ prints a line of hyphens for formatting. default length is 40 """
    print("-"*length)


def display(title):
    """ displays the title of the program 'nicely' """
    clear_screen()
    print(title.upper())
    hyphens()


def show_menu():
    """ show the menu with options and get user choice """
    while True:
        clear_screen()
        display("CLI FLASHCARD APP")
        print("1. Review flashcards")
        print("2. Add new flashcards")
        print("q. Exit")
        hyphens()
        
        # loop to get user_choice and catch bad inputs
        user_choice = input("Choice (1/2): ")
        if user_choice == '1':
            return 'review'
        elif user_choice == '2':
            return 'add'
        elif user_choice.lower() == 'q':
            print()
            print("Exiting...")
            sleep(1.5)
            quit()
        else:
            continue
