# USEFUL METHODS THAT CAN BE REUSED IN VARIOUS SCRIPTS

def clear_screen(length=100):
    """ clears the console screen using new lines. default length is 100 """
    print("\n"*length)

def hyphens(length=40):
    """ prints a line of hyphens for formatting. default length is 40 """
    print("-"*length)

def get_time_seconds(units, duration):
    """ converts the time to seconds """
    if units == 's':
        return duration
    elif units == 'mins':
        return duration * 60
    else:
        return duration * 3600
