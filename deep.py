# Get the text from the user
text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
text = text.lower().strip()

# Match the user text
match text:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")