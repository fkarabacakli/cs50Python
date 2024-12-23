names = []

with open("names.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")