from cs50 import get_float

# reprompt user for change value until it is nonnegative
while True:
    change = get_float("Change: ")
    if change > 0:
        break
# convert dollars to cents
cents = round(change*100)

# diving by 25, outputting the nearest whole number, to get how many quarters to use
coins = cents // 25
# calculate how many cents remain
cents %= 25

# repeat for dimes and nickels, making sure to add onto previous value of coins
coins += cents // 10
cents %= 10
coins += cents // 5

# print total number of coins, which will be the previous number of coins + the remaining change, which is in pennies
print(coins + (cents % 5))