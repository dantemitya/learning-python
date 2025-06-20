def parse(data):
    """ parses comma separated data inputted by the user """
    start = 0 # index where to begin slice
    end = 0 # index where to end slice
    parsed = [] # the cleaned data without commos
    for index, char in enumerate(data):
        if char == ',':
            end = index
            parsed.append(data[start:end])
            start = end + 1

    # parse last number
    data = data[::-1]
    start = 0
    end = 0
    for index, char in enumerate(data):
        if char == ',':
            end = index
            temp = data[start:end]
            parsed.append(temp[::-1])
            break

    return parsed

data = "1,4,45,3,3,6234"

print(parse(data))
