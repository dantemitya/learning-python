import utils
from time import sleep

"""
goal: enter some text and then get word count, character count, most common words, etc.
to write:
    * text parser - prepare inputted text for anaylizing
    * word count function
    * character count function
    * common word counter function
    * make the program loop (i.e. doesn't quit after one execution)
    * make interactive menu so you can go back, exit
"""

def show_menu():
    """ show the main menu """
    while True:
        utils.display("TEXT ANALYZER")
        print("1. Analyze Text")
        print("0. Quit")
        utils.hyphens()
        choice = input("Choice: ")
        
        # exit menu function and return an execution code
        if choice == "1":
            return 1
        elif choice == "0":
            return 0
        else:
            continue

def main():
    menu = show_menu()
    
    # run the text analyzer if 1 is returned
    if menu == 1:
        utils.display("TEXT ANALYZER")
        user_input = input("Enter text to analyze: ")

        utils.display("TEXT ANALYZER")
        print("Analyzing text...")
        sleep(2)
        
        utils.display("TEXT ANALYZER")
        parsed = utils.parse(user_input)
        print(parsed)
    
    # quit if 1 not returned
    else:
        quit()

if __name__ == '__main__':
    main()
