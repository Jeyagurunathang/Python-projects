# First import the all requiring modules

from pyfiglet import Figlet
from random import choice
import sys

# Store the Figlet Function in one variable
figlet = Figlet()

def main():

    # Check the length of the argv is 1 (or) not [or] literally no arguments
    if len(sys.argv) == 1:

        # Get input from the user
        text = get_input()

        # Because of no arguments.So, we need to pick a random text
        rand = choice(figlet.getFonts())
        figlet.setFont(font = rand)

        # And finally print the output for no argument type
        print(f"Output: {figlet.renderText(text)}")
        sys.exit()

    # Suppose user gives command-line arguments. So, check the length of command-line arguments is 3 (or) not
    elif len(sys.argv) == 3:

        # And now check the first user inputted command-line argument is [-f (or) --font] and scroll down read the check function
        if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and check() == True:

            # Now get the user input
            text = get_input()

            # Now they give command-line arguments. So, we don't need to get random font from getFonts() function.Instead we can use user's second command-line argument
            figlet.setFont(font = sys.argv[2])

            # Now print the output
            print(f"Output: {figlet.renderText(text)}")
            sys.exit()

        # If user's first command-line argument is not [-f (or) --font] simply print the statement and exit the program
        else:
            sys.exit("Output: Invalid usage")

    # If user inputted command-line argument is very low (or) very large simply print the statement and exit the program
    else:
        sys.exit("Output: Invalid usage")

# This function is used to check the user's second command-line argument(font-style) present in getFonts() function (or) not
def check():
    for i in figlet.getFonts():
        if sys.argv[2] == i:
            return True

# Get input from user's and return it
def get_input():
    text = input("Input: ").strip()
    return text

main()