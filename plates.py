def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Initialize a variable to store numbers
    num = 0

    # Get the first two letters from the users input
    x = s[:2]

    # Find how many numbers are present in the users text
    for i in s:
        if i.isdigit() == True:
            num += 1

    # Get the characters after first two letters
    n = list(s[num:])
    f = n[0] # First letter in the n substring
    l = n[-1] # Last letter in the n substring

    # Check the values
    if len(s) <= 6 and x.isalpha() == True and len(x) == 2:
        if num == 0:
            return True
        elif (f.isdigit() == True or f.isalpha() == True) and f != '0' and l.isdigit() == True:
            return True
    else:
        return False


main()