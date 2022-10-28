# Prompt the user to type a camelcase text
text = input("camelCase: ").strip()

# Check each character in the user text for any upper character and print snakecase
print("snake_case: ", end="")
for t in text:
    if t.isupper() == True:
        print(f"_{t.lower()}", end="")
    else:
        print(t.lower(), end="")
print()