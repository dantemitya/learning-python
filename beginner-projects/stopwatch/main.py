# STOPWATCH

import time
import utils

def main():
    # initialize time variables
    seconds = 0
    hours = 0
    mins = 0

    while True:
        # display title
        utils.clear_screen()
        print("STOPWATCH")
        utils.hyphens()
        
        # check seconds to change minutes
        if seconds == 60:
            seconds = 0
            mins += 1
        
        # check mins to change hours
        if mins == 60:
            mins = 0
            hours += 1
        
        # automatically quit program once 24 hours have passed
        # so that the clock doesn't carry on indefinitely
        if hours == 24:
            quit()
        
        # output the time in a nice formatted manner
        print(f"{hours:02d}:{mins:02d}:{seconds:02d}")

        # the actual counter using the sleep method from the time module
        seconds += 1
        time.sleep(1)

if __name__ == "__main__":
    main()
