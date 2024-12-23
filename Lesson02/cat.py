def get_number():
    while True:
        i = input("How many time ? ").strip()
        if i.isnumeric():
            i = int(i)
            return i

def meow(i):
    for _ in range(i):
        print("meow")

def main():
    n = get_number()
    meow(n)

main()