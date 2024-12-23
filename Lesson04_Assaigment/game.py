import random

def get_int(s):
    while True:
        i = input(s).strip()
        if i.isnumeric():
            return int(i)
        else:
            print("Invalid, it must be integer!!")

def main():
    level = get_int("Level: ")
    picked_number = random.randint(1,level)
    
    while True:
        guess = get_int("Guess: ")
        if guess > level:
            print("Guess can not be bigger than level")
        elif guess>picked_number:
            print("Too large!")
        elif picked_number>guess:
            print("Too small!")
        elif guess==picked_number:
            print("Just right!")
            break

if __name__ == "__main__":
    main()