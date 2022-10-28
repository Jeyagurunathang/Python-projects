# Prompt the user to type some text
text = input("Input: ").strip()

# Create vowels list
vowels = ['a', 'e', 'i', 'o', 'u']
Vowels = ['A', 'E', 'I', 'O', 'U']

# Find any vowels are present in the user's text and replace it
for i in vowels:
    text = text.replace(i, "")

for j in Vowels:
    text = text.replace(j, "")

print("Output:", text)