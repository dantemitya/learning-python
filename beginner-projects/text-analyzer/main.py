import utils
from time import sleep
import nltk
from nltk.corpus import words

# for word count
nltk.download('words')
english_words = set(w.lower() for w in words.words())

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

def run_parser(exec_code):
    """ runs the loop for parsing text """
    # run the text analyzer if 1 is returned
    if exec_code == 1:
        utils.display("TEXT ANALYZER")
        user_input = input("Enter text to analyze: ")

        utils.display("TEXT ANALYZER")
        print("Analyzing text...")
        sleep(2)
        
        utils.display("TEXT ANALYZER")
        parsed = utils.parse(user_input)
        return parsed
    
    # quit if 1 not returned
    else:
        quit()

def word_count(text):
    """ use nltk corpus to count English words """
    words = [word for word in text if word in english_words]
    return len(words)

def main():
    # show the menu and let user choose option
    menu = show_menu()
    
    while True:
        # parse the inputted text for processing
        parsed = run_parser(menu)

        # run word count check
        count = word_count(parsed)
        print(f"Word count: {count}")
        utils.hyphens()

        # prompt to continue or quit
        while True:
            print("Would you like to analyze more text or quit?")
            print("1. Analyze more text")
            print("0. Quit")
            choice = input("Choice: ")

            if choice == '1':
                break
            else:
                quit()

if __name__ == '__main__':
    main()
