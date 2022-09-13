def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    # First we need to remove the symbol and we can convert to float for no bugs
    d = d.replace("$", "")
    return float(d)


def percent_to_float(p):
    # TODO
    # First we need to remove the symbol and we can convert to float for no bugs
    p = p.replace("%", "")
    return float(p) / 100

main()
