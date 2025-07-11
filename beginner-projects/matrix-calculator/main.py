# MATRIX CALCULATOR PROGRAM
import utils


def main():
    while True:
        choice = utils.menu()
        utils.parseChoice(choice)


if __name__ == '__main__':
    main()

