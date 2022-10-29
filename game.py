# Import the required modules
import random
import sys

def main():

    # Use while loop to iterate it whole program
    while True:

        # Get input level from the user by level function
        text = level()

        # Get a random number(answer) from the randint function in the random module
        ans = random.randint(1,text)

        # Get a guess number from the user by using guessing function
        guess = guessing()

        # Check the user's guessed value is matched to our guessed values (or) not
        checking(ans, guess)

def level():

    # Use while loop to iterate whole time to get correct level from the user
    while True:

        # Use try and except to catch the errors like (giving string input for level (or) giving negative integer)
        try:
            text = int(input("Level: "))
        except:
            pass
        else:
            # Check the user's inputted level is not negative integer (or) zero
            if text <= 0:
                pass
            else:
                return text

def guessing():

    # Use while loop to iterate whole time to get correct guess from the user
    while True:

        # Use try and except to catch the errors like (giving string input for guess (or) giving negative integer)
        try:
            guess = int(input("Guess: "))
        except:
            pass
        else:
            # Check the user's guess is not negative integer (or) zero
            if guess < 0:
                pass
            else:
                return guess

def checking(ans, guess):

    # Use while loop to iterate whole time to check the user's guess is matched to our answer (or) not
    while True:
        if guess > ans:
            print("Too large!")
            guess = guessing()
        elif guess < ans:
            print("Too small!")
            guess = guessing()
        else:
            print("Just right!")
            sys.exit()

if __name__ == "__main__":
    main()