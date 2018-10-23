from cs50 import get_string
from sys import argv


# make sure only 1 extra argument is provided. If not, exit and return 1.
if len(argv) != 2:
    print("Usage: ./caesar key")
    exit(1)

# Convert inputted key to integer
key = int(argv[1])

# get plaintext from user
plaintext = get_string("plaintext: ")

# To encrypt plaintext, add the key to each character. To make sure it loops around, subtract A, mod by 26, and then add A back again to get to the right section in ASCII numbers. However, separate upper case and lower case characters since they are in different sections of ASCII numbers.
print("ciphertext: ", end="")
for c in plaintext:
    if c.isupper():
        print(f"{chr(((ord(c) - ord('A') + key) % 26) + ord('A'))}", end="")
    elif c.islower():
        print(f"{chr(((ord(c) - ord('a') + key) % 26) + ord('a'))}", end="")
    # make sure non-letters don't change
    else:
        print(c, end="")

# print new line
print()
