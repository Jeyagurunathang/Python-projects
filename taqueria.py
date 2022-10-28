def main():
    total = 0
    foods ={
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    while True:
        n = check()
        for i in foods:
            if n == i:
                total += foods[i]
                print(f"Total: ${total:.2f}")
        if n == None:
            break

def check():
    while True:
        try:
            food = input("Item: ").title().strip()
            return food
        except EOFError:
            print()
            break

main()