import random


def main():
    score = int(0)
    level = get_level("Level: ")

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        print(f"{x} + {y} = ", end="")
        answer = get_int("")
        if answer == x + y:
            score += 1
        else:
            print("EEE")
    print(f"Score: {score}")


def get_level(s):
    while True:
        i = input(s).strip()
        if i.isnumeric():
            i = int(i)
            if i == 1 or i == 2 or i == 3:
                return i
        else:
            print("Invalid, Level must be integer!!")


def get_int(s):
    while True:
        i = input(s).strip()
        if i.isnumeric():
            return int(i)
        else:
            print("Invalid, it must be integer!!")


def generate_integer(level):
    if level == 1:
        return random.randrange(1, 9)
    elif level == 2:
        return random.randrange(10, 99)
    elif level == 3:
        return random.randrange(100, 999)


if __name__ == "__main__":
    main()
