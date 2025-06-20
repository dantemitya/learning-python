# USEFUL METHODS THAT CAN BE REUSED IN VARIOUS SCRIPTS

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

def length_check(password):
    """ runs a check against the length of the password and returns a score """
    if len(password) <= 8:
        return 1
    elif len(password) > 8 and len(password) < 16:
        return 2
    elif len(password) >= 16:
        return 3

def variety_check(password):
    """ character variety check """
    return 0

def entropy_check(password):
    """ check for unpredictability """
    return 0

def dict_check(password):
    """ check for common words and passwords """
    return 0

def patterns_check(password):
    """ check for keyboard patterns """
    return 0

def run_checks(password):
    """ run all of the check functions on a password """
    length_score = length_check(password)
    variety_score = variety_check(password)
    entropy_score = entropy_check(password)
    dict_score = dict_check(password)
    pattern_score = patterns_check(password)
    criteria = [length_score, variety_score, entropy_score, dict_score, pattern_score]
    score = sum(criteria) / len(criteria)
    return score

