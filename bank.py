# Get the text from the user
text = input("Greeting: ").lower().strip()

# Find the first two & first text in user text
x = text[:2]
y = text[:1]

# Check the first character is h and second character is he
if x == "he":
    print("$0")
elif y == "h":
    print("$20")
else:
    print("$100")