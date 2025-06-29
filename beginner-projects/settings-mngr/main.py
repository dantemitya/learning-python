# JSON SETTINGS MANAGER
import json
import utils
from time import sleep

filename = "settings.json"

def load_settings():
    """ loads the settings into a variable """
    with open(filename, "r") as f:
        settings = json.load(f)
    return settings


def show_settings(settings):
    """ print out the settings for the user """
    print("Current settings\n")
    for parent_key, child_dict in settings.items():
        print(f"Parent: {parent_key}")
        if isinstance(child_dict, dict):
            for child_key, value in child_dict.items():
                print(f"  {child_key}: {value}")
        else:
            print(f"  {child_dict}")
    utils.hyphens()


def save_settings(settings):
    """ write the updated data to the file and quit """
    with open(filename, "w") as f:
        json.dump(settings, f, indent=2)
    print("\nSaving changes...")
    sleep(1.5)
    print("Exiting...")
    sleep(1.5)
    quit()


def update_settings(settings, setting_name_parent, setting_name_child, update):
    """ update a particular setting within the .json file """
    settings[setting_name_parent][setting_name_child] = update
    print(f"\nValue of [{setting_name_parent}]|[setting_name_child] updated.")
    sleep(1.5)
    print("Please quit to save changes.")
    sleep(1.5)


def main():
    # load the settings in before anything else
    settings = load_settings()
    
    while True:
        # print title
        utils.display("JSON SETTINGS MANAGER")

        # show the settings for the user
        show_settings(settings)
       
       # get user choices
        while True:
            print("Enter 'q' to save and quit\n")
            
            # TODO: Add error handling for bad input for lines 65-77
            # parent key to access
            parent = input("Name of parent key to edit: ").lower()
            if parent.lower() == 'q':
                save_settings(settings)
            
            # child key to access within parent
            child = input(f"Name of child key in [{parent}] to edit: ").lower()
            if child.lower() == 'q':
                save_settings(settings)
            
            # value to update
            update = input(f"New value of [{parent}]|[{child}]: ")
            if update.lower() == 'q':
                save_settings(settings)

            # update the specified setting
            update_settings(settings, parent, child, update)
            break


if __name__ == "__main__":
    main()
