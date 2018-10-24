from cs50 import get_string
from sys import argv


def main():

    # make sure only 1 extra argument is provided
    if len(argv) != 2:
        print("Usage: python bleep.py dictionary")
        exit(1)

    # declare set
    words = set()

    # open file
    infile = open(argv[1])

    # read each line into set of words
    for line in infile:
        words.add(line.strip("\n"))

    # get message from user
    s = get_string("What message would you like to censor?\n")

    # split string into set of words
    message = s.split()

    # iterate through each word in message and compare with all words in dictionary
    for item in message:
        if item.lower() in words:
            print("*"*len(item), end="")
        else:
            print(item, end="")
        # print space after each word
        print(" ", end="")

    # print new line
    print()


if __name__ == "__main__":
    main()
