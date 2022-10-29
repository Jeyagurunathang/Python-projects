import inflect

p = inflect.engine()
def main():
    values = []
    while True:
        value = check()
        if value == None:
            break
        values.append(value)
    print(f"Adieu, adieu, to {p.join(values)}")

def check():
    while True:
        try:
            text = input("Name: ").strip()
            return text
        except EOFError:
            print()
            break

if __name__ == "__main__":
    main()