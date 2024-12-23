def print_meows(n:int) -> str:
    return "Meow\n"*n

number = int(input("Number: "))
meow = print_meows(number)
print(meow,end="")