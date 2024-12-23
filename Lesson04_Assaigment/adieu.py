
names = []

while True:
    string = input("Name: ")
    
    match string.strip():
        case "":
            break

    names.append(string.title())

length = len(names)
print("Adieu, adieu, to ",end="")
for i in range(length):
    
    if length==1:
        print(f"{names[i]}.")
    elif i==length-1:
        print(f"and {names[i]}.")
    elif i==length-2:
        print(f"{names[i]} ",end="")
    else:
        print(f"{names[i]}, ",end="")