def main():
    while True:
        n = get_fuel()
        if n <= 100:
            break

    # Find and print the fuel(Is it empty or not)
    if n <= 1:
        print("E")
    elif n >= 99 and n <= 100:
        print("F")
    else:
        print(f"{n}%")

def get_fuel():
    while True:
        try:
            text = input("Fraction: ")
            x, y = text.split('/')
            return round((int(x) / int(y)) * 100)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break

main()