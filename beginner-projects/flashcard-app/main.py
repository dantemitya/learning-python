# BASIC CLI FLASHCARD PROGRAM
# CREATE AND REVIEW FLASHCARDS
# STORE FLASHCARDS AND APP SETTINGS WITH JSON
import utils
import json
from time import sleep


filename = "flashcards.json"


# load the flashcards globally
with open(filename, "r", encoding="utf-8") as f:
    flashcards = json.load(f)


def add_flashcards():
    """ starts the add flashcards loop """
    while True:
        utils.display("ADDING FLASHCARDS")
        front = input("Front of flashcard: ")
        back = input("Back of flashcard: ")

        # make dict of card and add to flashcards
        make_new_card(front, back)
        print()
        print("New flashcard added")
        sleep(1.5)
        print()
        user_choice = input("Would you like to add another flashcard (y/n)?: ")
        if user_choice == 'y':
            continue
        else:
            add_new_cards()
            break


def make_new_card(front, back):
    """ defines a new flashcard """
    new_card = {
            "front": front,
            "back": back
            }
    flashcards.append(new_card)


def add_new_cards():
    """ adds all new flashcards to the json file """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(flashcards, f, indent=4, ensure_ascii=False)


# TODO: finish writing this function
def review_flashcards():
    """ starts the review flashcards loop """
    utils.display("REVIEWING FLASHCARDS")
    sleep(2)
    pass

def main():
    # print out program title
    utils.display("CLI FLASHCARD APP")
    
    while True:
        # get user choice
        user_choice = utils.show_menu()

        # either add or review based on user_choice
        if user_choice == 'add':
            add_flashcards()
            continue
        elif user_choice == 'review':
            review_flashcards()
            continue


if __name__ == '__main__':
    main()

