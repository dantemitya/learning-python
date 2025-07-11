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
        print("4. Get det, inverse, eigenvalues, etc.")
        print("q. Quit")
        hyphens()
        
        while True:
            print("Enter 1/2/3/4/q")
            choice = input("> ")
            if choice.lower() not in ['1','2','3','4','q']:
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
        quit()

def defMatrix(shape):
    """ inits a zero matrix with the specified shape """
    M = np.zeros((shape[0],shape[1]))
    return M


def getElements(matrix):
    """ get elements for a matrix """
    for rowindex,rowelement in enumerate(matrix):
        for colindex,colelement in enumerate(rowelement):
            print(f"\nEnter value for row {rowindex+1}, column {colindex+1}")
            matrix[rowindex,colindex] = float(input("> "))
            print()
    

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

            clear_screen()
            hyphens()
            print(f"\nMatrix 1:\n{matrix1}\n")
            print(f"Matrix 2:\n{matrix2}\n")
            hyphens()
            print(f"\nResult of addition:\n{result}\n")
            hyphens()
            
            print("Enter 'm' to go back to the menu")
            print("Enter any other key to continue")
            choice = input("> ")
            if choice.lower() == 'm':
                break
            else:
                continue


def subtractionMode():
    """ subtract matrices mode """
    while True:
        display("MATRIX SUBTRACTION")
        
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

            result = np.subtract(matrix1,matrix2)
            
            clear_screen()
            hyphens()
            print(f"\nMatrix 1:\n{matrix1}\n")
            print(f"Matrix 2:\n{matrix2}\n")
            hyphens()
            print(f"\nResult of subtraction:\n{result}\n")
            hyphens()
            
            print("Enter 'm' to go back to the menu")
            print("Enter any other key to continue")
            choice = input("> ")
            if choice.lower() == 'm':
                break
            else:
                continue
        

def multMode():
    """ multiply matrices mode """
    while True:
        display("MATRIX MULTIPLICATION")
        
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

        if shape1[1] != shape2[0]:
            print("\nError: Matrix dimensions must be the same.")
            print("Please try again.\n")
            sleep(3)
            continue
        else:
            matrix2 = defMatrix(shape2)
            getElements(matrix2)
            print(f"Matrix 2:\n{matrix2}")

            result = np.matmul(matrix1,matrix2)
            
            clear_screen()
            hyphens()
            print(f"\nMatrix 1:\n{matrix1}\n")
            print(f"Matrix 2:\n{matrix2}\n")
            hyphens()
            print(f"\nResult of multiplication:\n{result}\n")
            hyphens()
            
            print("Enter 'm' to go back to the menu")
            print("Enter any other key to continue")
            choice = input("> ")
            if choice.lower() == 'm':
                break
            else:
                continue


def infoMode():
    """ get matrix info """
    while True:
        display("MATRIX INFO")
        print("Define matrix")
        shape = getShape()
        if shape[0] != shape[1]:
            print("Error: must be a square matrix")
            print("Please try again")
            continue
        else:
            matrix = defMatrix(shape)
            getElements(matrix)
            clear_screen()
            print(f"Info for the matrix:\n{matrix}")
            hyphens()
            
            # determinant
            det = np.linalg.det(matrix)
            print(f"\nDet: {det:.4f}\n")
            
            # inverse
            print(f"Inverse:\n{np.linalg.inv(matrix)}\n")

            # trace
            print(f"Trace: {np.trace(matrix):.4f}\n")
            
            # norm
            print(f"Norm: {np.linalg.norm(matrix):.4f}\n")

            # eigenvalues and eigenvectors
            eigen = np.linalg.eig(matrix)
            print(f"Eigenvalues:\n{eigen[0]}\n\nEigenvectors:\n{eigen[1]}\n")

            # transpose
            print(f"Transpose:\n{np.linalg.matrix_transpose(matrix)}\n")

            hyphens()
            print("Enter 'm' to go back to the menu")
            print("Enter any other key to continue")
            choice = input("> ")
            if choice.lower() == 'm':
                break
            else:
                continue


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

