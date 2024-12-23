def get_int():
    while True:
        i = input("How many time ? ").strip()
        if i.isnumeric():
            i = int(i)
            return i

def mario_print(n):
    for _ in range(n) :
        print("#"*n)

def main():
    n = get_number()
    mario_print(n)
    
main()