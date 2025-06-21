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

def parse(text):
    """ parses a string, removes punctuation and numbers, and returns a list of words """
    words = text.split()
    cleaned = []

    for word in words:
        # Keep only alphabet characters
        new_word = ''.join(char for char in word if char.isalpha())
        if new_word: # only add non-empty words
            cleaned.append(new_word) # however skips words with hyphens or apostrophes
    
    return cleaned
