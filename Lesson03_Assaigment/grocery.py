items ={}

while True:
    try:
        item = input("Item: ").strip().upper()
        
        if item=="":
            break
        elif item in items:
            items[item]+=1
        else:
            item = {f"{item}":1}
            items.update(item)

    except EOFError:
        print("Invalid input!!")

for i in items:
    print(items[i],end=" ")
    print(i)