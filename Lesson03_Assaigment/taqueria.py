menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total=int(0)

while True:
    s = input("Item: ").title().strip()
    if s=="":
        break
    elif s in menu:
        total += menu[s]
        print(f"Total: ${total}")
    