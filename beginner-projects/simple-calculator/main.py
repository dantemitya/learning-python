""" Performs +, -, *, / on two numbers.
User selects the operation. """

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def div(a, b):
    return a / b

def mult(a, b):
    return a * b

print("====SIMPLE CALCULATOR====")
print()

while True:
    choice = input("What would you like to do (add/minus/div/mult)?: ")
    if choice == 'add':
        print()
        print("ADD")
        print()
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print(add(a,b))
        break
    elif choice == 'minus':
        print()
        print("SUBTRACT")
        print()
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print(minus(a,b))
        break
    elif choice == 'div':
        print()
        print("DIVIDE")
        print()
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print(div(a,b))
        break
    elif choice == 'mult':
        print()
        print("MULTIPLY")
        print()
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print(mult(a,b))
        break
    else:
        continue
