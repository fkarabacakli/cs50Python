from random import choice
choice = ["yazi","tura"]

user = int(0)
computer = int(0)

while True:
    guess = input("What is your guess? (Yazı / Tura)")
    coin = choice(choice)
    match guess.strip().lower():
        case "exit" | "e":
            break
        case "yazi" | "1":
            if coin=="yazi":
                print(f"Your guess is correct. ({coin})")
                user += 1
            else:
                print(f"Your guess is uncorrect. ({coin})")
                computer +=1
        case "tura" | "2":
            if coin=="tura":
                print(f"Your guess is correct. ({coin})")
                user += 1
            else:
                print(f"Your guess is uncorrect. ({coin})")
                computer +=1
        case _:
            print("Your command is invalid")
                

if computer>user:
    print(f"{user+computer} games played computer oynanan {computer} oyunu kazandı")
    print("----------Wınner is COMPUTER----------")
elif user>computer:
    print(f"{user+computer} games played user oynanan {user} oyunu kazandı")
    print("----------Wınner is USER----------")
elif computer==0 and user==0:
    pass
else:
    print(f"{user+computer} games played iki oyuncuda oynanan {user} oyunu kazandı")
    print("----------TIE----------")
