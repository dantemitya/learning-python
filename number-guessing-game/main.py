""" User has to guess a randomly generated number.
Give hints like too high or too low. """

# for generating random integers
from random import randint

print("====NUMBER GUESSING GAME====")

# generate the random number
number = randint(0, 100)

print("I am thinking of a number between 0 and 100...")
print()

# loop for giving the user hints and showing their guesses
guess_count = 0
while True:
    guess = int(input("Guess: "))
    guess_count += 1
    print()
    if guess < number:
        print("Too low!")
        print()
    elif guess > number:
        print("Too high!")
        print()
    elif guess == number:
        print("Correct - You win!")
        print(f"Number of gueses: {guess_count}")
        break
