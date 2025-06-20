# TODO: Need to fix the case where there is no mode (e.g. [1,2,3])

import utils

def main():
    # display title
    utils.display("STATS SUMMARY") 
    
    # get user input
    print("Enter all data separated by commas")
    user_input = input("Data: ")
    
    # parse the inputted string and convert it to a list
    data = utils.parse(user_input)

    # print out stats
    utils.clear_screen()
    print("Statistics for data")
    print(data)
    utils.hyphens()
    print(f"Mean: {utils.mean(data)}")
    print(f"Median: {utils.median(data)}")
    print(f"Mode: {utils.mode(data)}")
    print()

if __name__ == '__main__':
    main()

