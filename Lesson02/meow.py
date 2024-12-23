def n_print(x,string):
    for i in range(x):
        print(string)

def get_int(s):
    while True:
        i = input(s).strip()
        if i.isnumeric()==True:
            i = int(i)
            return i

def main():
    
    tekrar = get_int("How many time ")
    s = str(input("What is the string? "))
    n_print(tekrar,s.strip().title())

main()
