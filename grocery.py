def main():
    g_list = []
    g_d = {}
    while True:
        item = check()
        if item != None:
            # Store the user's input value in list and dictionary
            # Because list allows duplicate values
            # So we use list to count the values
            g_list.append(item)
            g_d[item] = 0
        else:
            break

    # Calculate function will calculate the grocery items by using list and dictionary
    calculate(g_list, g_d)

    # Printing function just use to print the dictionary in sorted way
    printing(g_d)

def check():
    while True:
        try:
            item = input("").strip()
            return item
        except EOFError:
            print()
            break

def calculate(g_list, g_d):
    # Get each value from the list
    for i in g_list:
        # Get each value from the dictionary
        for j in g_d:
            # Compare the two values whether they are equal or not
            if j == i:
                g_d[j] += 1

def printing(g_d):
    for i in sorted(g_d):
        print(g_d[i], end=" ")
        print(i.upper())

main()