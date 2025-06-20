def clear_screen(length=100):
    """ clears the console screen using new lines. default length is 100 """
    print("\n"*length)

def hyphens(length=40):
    """ prints a line of hyphens for formatting. default length is 40 """
    print("-"*length)

def add_task(todo):
    """ adds a task to the to-do list """
    
    # take a string from the user and add the-
    # capitalized version to the todo list
    user_input = input("Add something to your to-do list: ")
    todo.append(user_input.capitalize())

    clear_screen()

    # display a notification
    print(f"\n'{user_input.capitalize()}' was added to your to-do list.")

def read_list(todo):
    """ reads out the to-do list """
    index = 1
    for task in todo:
        print(f"{index}. {task}")
        index += 1
    hyphens()

def options():
    """ display the options to choose from """
    print("1. Add a task to the to-do list")
    print("2. Read out the to-do list")
    print("3. Delete a task from the to-do list")
    print("4. Clear the to-do list")
    print("5. Exit")
    hyphens()


