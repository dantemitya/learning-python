# A SIMPLE COUNTDOWN TIMER

import time
import utils

# input handling loop to get the user's desired time
while True:
    utils.clear_screen()
    print("COUNTDOWN TIMER")
    utils.hyphens()
    try:
        units = str(input("Select timer units (s/mins/hrs): "))
        if units == 's' or units == 'mins' or units == 'hrs':
            duration = int(input("Choose timer duration: "))
            time_in_seconds = utils.get_time_seconds(units, duration)
            utils.hyphens()
            break
    except ValueError:
        continue

# the code for the timer
while time_in_seconds >= 0:
    utils.clear_screen()
    print(f"Time duration: {duration} {units}")
    utils.hyphens()
    print(f"Time remaining: {time_in_seconds} s")
    time_in_seconds -= 1
    time.sleep(1)

utils.clear_screen()
print("Times up!")
