# DICE ROLL SIMULATOR

# for generating the face which each die shows
from random import randint

def roll_dice(n, f):
    """ roll n dice with f faces each, a single time each """
    throws = {}
    for die in range(1,n+1):
        throws[f"Throw {die}"] = randint(1,f)
    return throws

def display_results(results):
    """ display the results of the dice throws """
    for throw in results:
        print(f'{throw}: {results[throw]}')

def results_stats(results):
    """ statistics of roll_dice """
    sumr = []
    for throw in results:
        sumr.append(results[throw])
    return sum(sumr), min(sumr), max(sumr)


print()
no_of_dice = int(input("How many dice would you like to throw?: "))
faces = int(input("How many faces for each die?: "))

# get the results of the throws as well as the sum, smallest throw, and largest throw
results = roll_dice(no_of_dice, faces)
sumt, small, large = results_stats(results)

print()
display_results(results)
print()

# display statistics of the throws
print(f'Sum of all throws: {sumt}')
print(f'Smallest throw: {small}')
print(f'Largest throw: {large}')
print()
