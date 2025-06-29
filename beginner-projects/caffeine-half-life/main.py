import utils

HALF_LIFE_CAFFEINE = 5 # half-life of caffeine in hours; should be 3 < t < 10.

def half_life(caffeine, time):
    """find how much caffeine remains in someone's system after t hours"""
    C0 = caffeine  # initial caffeine amount in milligrams (mg)
    t = time * 3600  # time elapsed in hours converted to seconds
    hl = HALF_LIFE_CAFFEINE * 3600  # half-life of caffeine in seconds
    C = round(C0 * (0.5) ** (t / hl), 2)  # caffeine amount at time t
    return f"After {time} hours, the caffeine content should reduce to {C} mg."


def main():
    utils.display("CAFFEINE HALF-LIFE")
    
    while True:
        try:
            caffeine = float(input("How much caffeine did you consume? (mg): "))
            break
        except ValueError:
            continue
    while True:
        try:    
            time = float(input("Hours elapsed since consumption: "))
            break
        except ValueError:
            continue
    
    print()
    print(half_life(caffeine, time))


if __name__ == "__main__":
    main()

