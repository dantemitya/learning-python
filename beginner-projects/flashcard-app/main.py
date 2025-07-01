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
    """starts the add flashcards loop"""
    card_id = int(get_id_start()) + 1  # get id of last card
    while True:
        utils.display("ADDING FLASHCARDS")
        front = input("Front of flashcard: ")
        back = input("Back of flashcard: ")

        # make dict of card and add to flashcards
        make_new_card(front, back, card_id)
        card_id += 1
        print()
        print("New flashcard added")
        sleep(0.25)
        print()
        user_choice = input("Would you like to add another flashcard (y/n)?: ")
        if user_choice == "y":
            continue
        else:
            update_json()
            break


def make_new_card(front, back, card_id, interval=1, state="new", reviews=0, lapses=0):
    """defines a new flashcard"""
    new_card = {
        "front": front,
        "back": back,
        "id": card_id,
        "interval": interval,  # days until next review
        "state": state,  # new/learning/learned
        "reviews": reviews,  # successful reviews count
        "lapses": lapses,  # number of failures
    }
    flashcards.append(new_card)


def get_id_start():
    """gets id of the last card in flashcards.json"""
    return flashcards[-1]["id"]


def update_json():
    """writes new data to the json file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(flashcards, f, indent=4, ensure_ascii=False)

# TODO: make it so that cards wont show up depending on their interval
# will need to use datetime for that
def review_flashcards():
    """starts the review flashcards loop"""
    while True:
        # loop through all flashcards and get feedback
        counter = 1
        for flashcard in flashcards:
            utils.display("REVIEWING FLASHCARDS")

            if flashcard["id"] != "0":  # ignore template card
                # show front of card and wait for user to continue
                print(f"\t\tCARD {counter}\n")
                print(f"FRONT: {flashcard['front']}")
                utils.hyphens()
                user_choice = input("Enter any key to see answer: ")

                # show back of card
                utils.display("REVIEWING FLASHCARDS")
                print(f"\t\tCARD {counter}\n")
                print(f"FRONT: {flashcard['front']}")
                print(f"BACK: {flashcard['back']}\n")

                # get user feedback on whether or not they passed
                utils.hyphens()
                print("Did you pass or fail the card?")
                result = input("Enter any key to pass or 'f' to fail: ")
                if result.lower() == "f":
                    # if the card is failed then reset its interval and reset state
                    flashcard["interval"] = "1"
                    flashcard["state"] = "learning"

                    # increment lapses by 1
                    lapses = int(flashcard["lapses"]) + 1
                    flashcard["lapses"] = str(lapses)

                    # reset reviews to 0
                    flashcard["reviews"] = "0"

                else:
                    # if the card is passed then double interval and change state
                    interval = int(flashcard["interval"]) * 2
                    flashcard["interval"] = str(interval)

                    # increment successful review counter
                    reviews = int(flashcard["reviews"]) + 1
                    flashcard["reviews"] = str(reviews)

                    # change state based on interval
                    if (
                        int(flashcard["interval"]) >= 21
                        or int(flashcard["reviews"]) >= 4
                    ):
                        flashcard["state"] = "learned"
                    else:
                        flashcard["state"] = "learning"

                    # reset lapses
                    flashcard["lapses"] = "0"

                counter += 1
                utils.clear_screen()

            else:
                continue

        # update the json file
        update_json()
        print("Reviewing finished")
        sleep(1.5)
        break


def main():
    # print out program title
    utils.display("CLI FLASHCARD APP")

    while True:
        # get user choice
        user_choice = utils.show_menu()

        # either add or review based on user_choice
        if user_choice == "add":
            add_flashcards()
            continue
        elif user_choice == "review":
            review_flashcards()
            continue


if __name__ == "__main__":
    main()
