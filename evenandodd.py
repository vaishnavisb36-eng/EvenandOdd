import sys


def even_and_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


if __name__ == "__main__":
    number = int(sys.argv[1])
    print("Number is:", even_and_odd(number))