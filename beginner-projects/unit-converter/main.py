import converters
import utils

# dictionary of the possible converters to choose from
options = {
        "1" : converters.cel_to_fah,
        "2" : converters.fah_to_cel,
        "3" : converters.mil_to_km,
        "4" : converters.km_to_mil,
        "5" : converters.lbs_to_kg,
        "6" : converters.kg_to_lbs
}

# list of the name of each converter for display purposes
converter_names = ["CELSIUS > FAHRENHEIT",
                   "FAHRENHEIT > CELSIUS",
                   "MILES > KILOMETERS",
                   "KILOMETERS > MILES",
                   "POUNDS > KILOGRAMS",
                   "KILOGRAMS > POUNDS"]

def main():
    utils.clear_screen()
    print("UNIT CONVERTER")
    utils.hyphens()
    
    # main loop
    while True:
        # menu for the user to see that available converters
        index = 0
        for name in converter_names:
            print(f"{index+1}. {converter_names[index]}")
            index += 1
        print("Enter 'q' to quit")
        utils.hyphens()
        
        # try/except block to catch bad inputs and for selecting a converter
        try:
            converter_selection = input("Choose a converter: ")
            if converter_selection == '0':
                converter_selection = '1'
            if converter_selection == 'q':
                quit()
            converter_name_index = int(converter_selection) - 1
            prompt_text = converter_names[converter_name_index]
        except (ValueError, IndexError):
            utils.clear_screen()
            continue
        
        # initliaze the answer for display purposes
        answer = 0
        while True:
            try:
                utils.clear_screen()
                print("Enter 'b' to go back to the menu")
                utils.hyphens()
                print(f"Answer: {answer}")

                # run the selected converter; again use try/except to catch bad inputs
                to_convert = input(f"{prompt_text}: ")
                if to_convert == 'b':
                    utils.clear_screen()
                    break
                to_convert_float = float(to_convert)
                answer = round(options[converter_selection](to_convert_float),4)
            except ValueError:
                continue

if __name__ == '__main__':
    main()

