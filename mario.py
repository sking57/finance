from cs50 import get_int

# continue to prompt user for integer until input is between 1 and 8
while True:
    height = get_int("Height: ")
    if height >= 1 and height <= 8:
        break
# print i+1 hashes in each row and (height-i-1) spaces in each row
for i in range(height):
    print(" " * (height - i - 1), end="")
    print("#" * (i+1))

