def main():
    # Get the time from the user
    time = input("What time is it? ").strip()
    t = convert(time)
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")
    else:
        print(end="")

def convert(time):
    h, m = time.split(":")
    h, m = float(h), float(m)
    times = ((h * 60) + m) / 60
    return times

if __name__ == "__main__":
    main()