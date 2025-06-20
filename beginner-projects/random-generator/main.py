# RANDOM DATA GENERATOR

# TODO: make the program a loop and add back and quit functionality

import utils
from random import randint
from faker import Faker

# for random names
fake = Faker()

def rand_num(mini, maxi):
    """ gets a random number from within a range """
    return randint(mini, maxi)

def rand_name():
    """ returns a random forename """
    return fake.first_name()

def rand_email():
    """ generates a random email """
    return fake.email()

def main():
    while True:
        # print title and menu
        utils.display("RANDOM DATA GENERATOR")
        print("1. Random number generator")
        print("2. Random forename generator")
        print("3. Random email generator")
        utils.hyphens()

        # get user input choice (either 1 or 2)
        choice = input("Choice: ")
        
        # user chooses to generate a random number
        if choice == '1':
            utils.clear_screen()
            print("Define the range")
            mini = int(input("Lower bound (integer): "))
            maxi = int(input("Upper bound (integer): "))
            utils.clear_screen()
            print(f"Random number generated between {mini} and {maxi}: {rand_num(mini, maxi)}")
            break
        
        # user chooses to generate a random name
        elif choice == '2':
            utils.clear_screen()
            print(f"Random forename generated: {rand_name()}")
            break

        # user chooses to generate a random email
        elif choice == '3':
            utils.clear_screen()
            print(f"Random email generated: {rand_email()}")
            break

        # continue loop for bad inputs
        else:
            continue

if __name__ == '__main__':
    main()

