# Import the emoji module
import emoji

# Get input from the user
text = input("Input: ")

# Convert the user input(emoji text) to emoji
output = emoji.emojize(text, language = "alias")

# Print the output
print(f"Output: {output} ")