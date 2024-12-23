from random import randint, choice as chooice

def main():
    question = "1) Guess Number\n2) RSP Game\n3)Reach Number\n--------------------------\nWhich game would you like to play? "
    while True:
        answer = input(question)
        if answer=="1":
            which_number()
            break
        elif answer=="2":
            rsp_game()
            break
        elif answer=="3":
            reach_number()
            break
        else:
            print("Invalid Command!!")

def which_number():
    number = get_int("Maksimum Numara: ")
    choice = randint(0,number)
    maksimum ,minimum , try_number= number,int(0),int(0)
    
    while True:
        guess = get_int("What is your guess: ")
        
        if guess==choice:
            print("It was correct number...")
            try_number +=1
            break
        elif guess <= minimum or guess >= maksimum:
            print(f"Number is between {minimum}-->{maksimum}")
        elif guess > choice:
            print(f"It is smaller than {guess}")
            maksimum = guess
            try_number += 1
        elif guess < choice:
            print(f"It is bigger than {guess}")
            minimum = guess
            try_number +=1
    
    print(f"You found in {try_number} try...")
    return 1


def rsp_game():
    user = int(0)
    computer = int(0)
    choices = [
        "rock",
        "paper",
        "scissors"
    ]
    
    while True:
        choice = chooice(choices)
        guess = input("What is your guess? (rock|paper|scissors) ---> ").strip().lower()
        match guess:
            case "rock":
                if choice == "rock":
                    print("Tie")
                    computer += 1
                    user += 1
                elif choice == "paper":
                    print("You lost.")
                    computer +=3
                elif choice == "scissors":
                    print("You won.")
                    user += 3
            case "paper":
                if choice == "rock":
                    print("You won.")
                    user += 3
                elif choice == "paper":
                    print("Tie")
                    computer += 1
                    user += 1
                elif choice == "scissors":
                    print("You lost.")
                    computer +=3
            case "scissors":
                if choice == "rock":
                    print("You lost.")
                    computer +=3
                elif choice == "paper":
                    print("You won.")
                    user += 3
                elif choice == "scissors":
                    print("Tie")
                    computer += 1
                    user += 1
            case "exit":
                if user > computer:
                    print(f"User won match with {user} point.")
                    return 1
                elif computer > user:
                    print(f"Computer won match with {computer} point.")
                    return 1
                else:
                    print(f"Game is tie...")
                    return 1
            case _:
                print("Invalid Command")


def reach_number():
    n = get_int("Which number would you like to reach? ")
    
    while True:
        i = get_int("How many Bomb: ")
        if i>0 and i<n:
            break

    bombs = []
    while len(bombs)<i:
        bomb = randint(0,n-1)
        if bomb not in bombs:
            bombs.append(bomb)    
    start = 0
    print(bombs)
    while True:
        next_number = get_int(f"{start}: ")
        if next_number <0 or next_number+ start > n:
            print("It must be between 0 to n")
        elif next_number>4:
            print("You can add max 4 in one time.")
        else:
            start += next_number
            if start == n:
                print("You wonn..")
                return 1
            elif start in bombs:
                print("You lost.")
                return 1
            
        


def get_int(s):
    
    while True:    
        try:
            i = input(s)
            if i.strip().lower()=="exit":
                exit()
            return int(i)
        except ValueError:
            print("It must be integer..  ",end="")

if __name__ == "__main__":
    main()