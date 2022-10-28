months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    # Get input from the user
    date = (input("Date: ")).strip()

    # Store the input to another variable for backup purpose
    backup_date = date

    # Replace the punctuation characters with whitespace in the user's original input not the backup one
    for i in date:
        if i == "/" or i == ",":
            date = date.replace(i, " ")

    # Split and store the replaced values into three variables
    m, d, y = date.split()

    # Do a partition in backup variable for find any comma's are present
    comma = backup_date.partition(d)

    # Store the last value from the partition variable
    find_comma = comma[2]

    # First check the month is not inputted alphabetically
    if m.isalpha() == False:
        # Check the month and date are not exceed 12 and 31 and also check the date is not inputted as characters else pass it
        if int(m) <= 12 and d.isalpha() == False and int(d) <= 31:
            print(y, end="-")
            print(f"{int(m):02}", end="-")
            print(f"{int(d):02}")
            break
        else:
            pass

    # Now we check if the month is inputted as characters
    else:
        # First we need to find the comma is present are not
        if find_comma[0] == ",":
            # Second find the month is presented in the months list are not
            count = months.count(m)
            # If the month is present increment the value with the appropriate month index value
            if count > 0  and int(d) <= 31:
                print(y, end="-")
                print(f"{int(count) + months.index(m):02}", end="-")
                print(f"{int(d):02}")
                break
            # If the month is not present just pass it
            else:
                pass
        # If any comma's are not in the user's input just pass it
        else:
            pass