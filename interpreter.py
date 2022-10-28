# First get the operation from the user
text = input("Experssion: ").strip()

# Split the operation given by user
x, y, z = text.split()
x, z = float(x), float(z)

# Do a operation depend on intermediate operator
match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case _:
        print(x / z)