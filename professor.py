import random

def main():
    score = 10
    level = get_level()
    for i in range(10):
        a, b = generate_integer(level)
        ans = get_ans(a, b)
        tot = a + b
        if ans != tot:
            score = checker(score, tot, a, b)
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level <= 3:
                return level
        except ValueError:
            pass

def generate_integer(level):
    match level:
        case 1:
            x, y = random.randint(0, 9), random.randint(0, 9)
            return x, y
        case 2:
            x, y = random.randint(10, 99), random.randint(10, 99)
            return x, y
        case 3:
            x, y = random.randint(100, 999), random.randint(100, 999)
            return x, y 

def get_ans(a, b):
    try:
        ans = int(input(f"{a} + {b} = "))
        return ans
    except ValueError:
        pass

def checker(score, tot, a, b):
    chance = 2
    while chance != 0:
        print("EEE")
        ans = get_ans(a, b)
        if ans == tot:
            break
        chance -= 1
    else:
        print("EEE")
        print(f"{a} + {b} = {tot}")
        score -= 1
    return score

if __name__ == "__main__":
    main()