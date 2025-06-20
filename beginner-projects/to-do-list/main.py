# TO-DO LIST (IN MEMORY)
import utils

utils.clear_screen()
print("TO-DO LIST")
utils.hyphens()

def main():
    
    # initialize the to-do list
    todo = []
    
    while True:
        # display the options that the user can choose from
        utils.options()

        # get the user input and then perform an action based on that
        user_input = input("What would you like to do?: ")
        
        # add a task to the to-do list
        if user_input == '1':
            utils.clear_screen()
            utils.add_task(todo)
            utils.hyphens()
        
        # read out the to-do list
        elif user_input == '2':
            utils.clear_screen()

            # let the user know if the list is already empty
            if len(todo) == 0:
                print("Your to-do list is empty.")
                utils.hyphens()
            else:
                utils.read_list(todo)

        # delete a task from the to-do list
        elif user_input == '3':
            utils.clear_screen()

            # let the user know if the list is already empty
            if len(todo) == 0:
                print("Your to-do list is empty, so there's nothing to delete.")
                utils.hyphens()
            else:
                while True:
                    utils.read_list(todo)
                    print()
                    try:
                        index_to_delete = int(input("Which task would you like to delete?: "))
                        removed = todo.pop(index_to_delete - 1)
                        utils.clear_screen()
                        print(f"'{removed}' was removed from your to-do list")
                        utils.hyphens()
                        break
                    except ValueError:
                        utils.clear_screen()
                        continue
        
        # clear the entire to-do list
        elif user_input == '4':
            utils.clear_screen()
            todo = []
            print("Your to-do list has been cleared")
            utils.hyphens()

        # exit sequence
        elif user_input == '5':
            quit()
        else:
            continue

if __name__ == '__main__':
    main()

