def main():
    hello()

def hello():
    while True: 
        name = input("What is your name? ").strip().title()
        word = len(name.split())
        if word == 0:
            print("Please write a name!!")
        elif word == 1:
            print(f"hello, {name}")
            return True
        elif word == 2:
            first, second = name.split(" ")
            print(f"hello, {first}")
            return True
        else:
            print("Uncorrect usage!!")
            print("You should use Only your first name...")
        
        
main()
