# USEFUL METHODS THAT CAN BE REUSED IN VARIOUS SCRIPTS
import numpy as np
from time import sleep


def clear_screen(length=100):
    """ clears the console screen using new lines. default length is 100 """
    print("\n"*length)


def hyphens(length=40):
    """ prints a line of hyphens for formatting. default length is 40 """
    print("-"*length)


def display(title):
    """ displays the title of the program 'nicely' """
    clear_screen()
    print(title.upper())
    hyphens()


def menu():
    """ show the options menu """
    while True:
        display("MATRIX CALCULATOR")
        print("1. Add two matrices")
        print("2. Subtract two matrices")
        print("3. Multiply two matrices")
        print("4. Get det, inverse, trace, transpose")
        print("5. Get eigenvalues and eigenvectors")
        hyphens()
        
        while True:
            print("Enter 1/2/3/4/5")
            choice = input("> ")
            if choice not in ['1','2','3','4','5']:
                break
            else:
                return choice


def parseChoice(choice):
    """ parse the user choice and execute the specified loop """
    if choice == '1':
        additionMode()
    elif choice == '2':
        subtractionMode()
    elif choice == '3':
        multMode()
    elif choice == '4':
        infoMode()
    else:
        eigenMode()

def defMatrix(shape):
    """ inits a zero matrix with the specified shape """
    M = np.zeros((shape[0],shape[1]))
    return M

# TODO: finish writing this func
def getElements(matrix):
    """ get elements for a matrix """
    for rowindex,rowelement in enumerate(matrix):
        for colindex,colelement in enumerate(rowelement):
            print(f"\nEnter value for row {rowindex+1}, column {colindex+1}")
            matrix[rowindex,colindex] = float(input("> "))
            print()
    

# TODO: do actual addition under the else condition part
def additionMode():
    """ add matrices mode """
    while True:
        display("MATRIX ADDITION")
        
        # get info for first matrix
        print("Matrix 1")
        shape1 = getShape()
        matrix1 = defMatrix(shape1)
        getElements(matrix1)
        print(f"Matrix 1:\n{matrix1}")
        
        # get info for second matrix
        hyphens()
        print("\nMatrix 2")
        shape2 = getShape()

        if shape1 != shape2:
            print("\nError: Matrix dimensions must be the same.")
            print("Please try again.\n")
            sleep(3)
            continue
        else:
            matrix2 = defMatrix(shape2)
            getElements(matrix2)
            print(f"Matrix 2:\n{matrix2}")

            result = np.add(matrix1,matrix2)

            hyphens()
            print(f"\nResult of addition:\n{result}\n")
            hyphens()
            sleep(4)


# TODO: finish writing this func
def subtractionMode():
    """ subtract matrices mode """
    display("MATRIX SUBTRACTION")
    pass


# TODO: finish writing this func
def multMode():
    """ multiply matrices mode """
    display("MATRIX MULTIPLICATION")
    pass


# TODO: finish writing this func
def infoMode():
    """ get matrix info """
    display("MATRIX INFO")
    pass


# TODO: finish writing this func
def eigenMode():
    """ get eigenvalues and eigenvectors """
    display("EIGENVALUES & EIGENVECTORS")
    pass


def getShape():
    """ gets the shape of a matrix from the user """
    while True:
        try:
            rows = int(input("Number of rows: "))
            break
        except ValueError:
            continue

    while True:
        try:
            columns = int(input("Number of columns: "))
            break
        except ValueError:
            continue

    shape = [rows, columns]

    return shape

