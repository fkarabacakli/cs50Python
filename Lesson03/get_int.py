def get_int(s):
    while True:
        try:
            x = int(input(s))
            return x
        except ValueError:
            print("X must be an integer!! ",end="")

def main():
    i = get_int("What is x => ")
    print(i)
    
main()

# Raise make your own library for python