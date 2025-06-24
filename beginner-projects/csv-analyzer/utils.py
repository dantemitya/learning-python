# USEFUL METHODS THAT CAN BE REUSED IN VARIOUS SCRIPTS
import csv

def clear_screen(length=100):
    """ clears the console screen using new lines. default length is 100 """
    print("\n"*length)

def hyphens(length=80):
    """ prints a line of hyphens for formatting. default length is 40 """
    print("-"*length)

def display(title):
    """ displays the title of the program 'nicely' """
    clear_screen()
    print(title.upper())
    hyphens()

def get_csv(filename):
    """ get the csv and its header name for storing in a variable """
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames # header names
        return headers, list(reader) 

def show_csv(headers, data):
    """ read a csv file """
    print(headers)
    hyphens()
    for row in data:
        for header in headers:
            print(row[header], end='\t')
        print()

def get_column_data(key_column, value_column, data):
    """ returns specified column data as a dict """
    column_data = {}
    for row in data:
        column_data[row[key_column]] = row[value_column]
    return column_data

def get_min(column_data):
    """ gets the smallest value from a column along with the id """
    min_id = min(column_data, key=lambda k: float(column_data[k]))
    min_val = float(column_data[min_id])
    print(f"Lowest - {min_val} (ID: {min_id})")

def get_max(column_data):
    max_id = max(column_data, key=lambda k: float(column_data[k]))
    max_val = float(column_data[max_id])
    print(f"Highest - {max_val} (ID: {max_id})")
    
def get_avg(column_data):
    """ gets the average value from a column """
    values = [float(value.strip()) for value in column_data.values()]
    average = sum(values) / len(values)
    print(f"Average - {average:.1f}")


