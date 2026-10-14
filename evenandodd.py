import sys


def even_and_odd(number):
    if number % 2 == 0:
        return "Even number"
    return "Odd number"


if __name__ == "__main__":
    number = int(sys.argv[1])
    print(even_and_odd(number))