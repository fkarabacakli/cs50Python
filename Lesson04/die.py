from random import randint

while True:
    answer = input("Do you want to rool dice? ")
    match answer.strip().lower():
        case "yes" | "1":
            print(randint(1,6))
        case "no" | "2":
            break
