def get_int(s):
    while True:
        i = input(s).strip()
        if i.isnumeric():
            return int(i)
        else:
            print("Get integer!! ",end="")

def main():
    price = get_int("What is the price? ")
    coins = [25,10,5]
    cost = price
    while cost>0:
        print(f"Amount Due: {cost}")
        coin = get_int("Insert Coin: ")
        if coin in coins:
            cost -= coin
        else:
            print("Only 25, 10 and 5 valid!!!")
    
    if cost==0:
        print(f"Change Owed: {cost}")
    else:
        print(f"Change Owed: {cost+coin}")

    
main()