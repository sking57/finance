import sys
from cs50 import get_string


def main():

    # Ensure proper usage
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        exit("Usage: python slant.py depth")
    depth = int(sys.argv[1])

    # Encrypt message
    message = get_string("Message: ")
    if len(message) >= depth:
        print("Slanted:", slant(message, depth))


def slant(message, depth):
    chars = list(message)
    array = []
    # fill array with each (depth)th character of the message
    for i in range(depth):
        for j in range(i, len(message), depth):
            array.append(chars[j])
    # return array as joined string instead of list of characters
    return "".join(array)


if __name__ == "__main__":
    main()
