def clear_screen(length=100):
    """ clears the console screen using new lines. default length is 100 """
    print("\n"*length)

def display(title):
    """ displays the title of the program 'nicely' """
    clear_screen()
    print(title.upper())
    hyphens()

def hyphens(length=40):
    """ prints a line of hyphens for formatting. default length is 40 """
    print("-"*length)

def parse(data):
    """ parses comma separated data inputted by the user """
    start = 0 # index where to begin slice
    end = 0 # index where to end slice
    cleaned = [] # the cleaned data without commos
    for index, char in enumerate(data):
        if char == ',':
            end = index
            cleaned.append(data[start:end])
            start = end + 1

    # parse last number
    data = data[::-1]
    start = 0
    end = 0
    for index, char in enumerate(data):
        if char == ',':
            end = index
            temp = data[start:end]
            cleaned.append(temp[::-1])
            break
    
    # convert all data to integers
    parsed = []
    for num in cleaned:
        parsed.append(float(num))

    return parsed

def mean(data):
    """ returns the mean of a list of numbers """
    return round((sum(data) / len(data)),4)

def median(data):
    """ returns the median of a list of numbers """
    # sort the data in ascending order
    data.sort()

    # even number of data
    if len(data) % 2 == 0:
        return round(((data[int((len(data) // 2) - 1)] + data[int(len(data) // 2)]) / 2),4) 
    
    # odd number of data
    elif len(data) % 2 != 0:
        return round((data[int(len(data) // 2)]),4)

def mode(data):
    """ returns the mode of a list of numbers """
    # sort the data in ascending order
    data.sort()
    
    # keep a score for each number in a dictionary
    scores = {}
    for num in data:
        if num in scores:
            scores[num] += 1
        else:
            key = num
            scores[key] = 1
    return max(scores, key=scores.get)

