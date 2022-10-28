# First get the text from the user
text = input("File name: ").lower().strip()

# Find the extension file type
text = text.rpartition('.')
t = text[2].strip()

# Print the extension file type
match t:
    case "gif":
        print("image/gif")
    case "jpeg" | "jpg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print(f"text/{text[0]}")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")