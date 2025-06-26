# JSON SETTINGS MANAGER
import json

filename = "settings.json"

def load_settings(filename):
    with open(filename, "r") as f:
        settings = json.load(f)
    return settings

def main():
    settings = load_settings(filename)
    print(settings)

if __name__ == "__main__":
    main()
