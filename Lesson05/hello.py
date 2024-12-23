def main():
    name = input("Wat is your name? ")
    print(hello(name))

def hello(string="world"):
    if string.strip() == "":
        string = "world"
    return f"hello, {string.title().strip()}"

if __name__ == "__main__":
    main()
