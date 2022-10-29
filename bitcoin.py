# Import the required modules
import sys
import requests

def main():

    # Check the user provide's only one argument by using length function
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    # Check the argument provide by the user is not alphabetic
    elif sys.argv[1].isalpha() == True:
        sys.exit("Command-line argument is not a number")

    # Store the returned rate in amount variable
    amount = bitcoin_rate()

    # Convert the user's argument to float and multiple with the amount
    amount *= float(sys.argv[1])

    # Print the amount with thousand separator (comma after 3 digits)
    print(f"${amount:,.4f}")
    sys.exit()

def bitcoin_rate():

    # Get the json file by using requests module get function
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    # Store the json file in rate variable
    rate = response.json()

    # Enter the keys to get the rate
    keys = ["bpi", "USD", "rate_float"]

    # Using the keys list we can iterate over the json file and get the rate in float
    for key in keys:
        rate = rate.get(key)

    # After getting the rate return to the main function
    return rate

if __name__ == "__main__":
    main()