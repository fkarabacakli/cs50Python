balance = 0

def deposit(n):
    balance += n

def withdraw(n):
    balance -= n

def main():
    print("Balance:",balance)
    deposit(100)
    withdraw(50)
    print(balance)



if __name__ == "__main__":
    main()