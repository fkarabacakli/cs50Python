def main():
    s = str(input("What is string? "))
    twttr(s)

def twttr(string):
    vowels = ["a", "e", "i", "o", "u"]
    print("Output: ", end="")
    for i in string:
        if i.lower() not in vowels:
            print(i,end="")
    print()

main()
