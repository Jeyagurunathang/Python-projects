# Hardcode the amount for CS50 coke
amount = 50
change = 50

# Loop it untill amount is becomes zero
while amount > 0:
    print("Amount Due:", amount)
    coin = int(input("Insert Coin: "))

    # Change whether the user coin is (25, 10, 5) [or] not
    if coin == 25 or coin == 10 or coin == 5:
        amount -= coin
        change -= coin

# Print the change by multiplying with negative
print("Change Owed:", -change)