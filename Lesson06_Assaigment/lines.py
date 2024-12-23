import sys

def main():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-3:]!=".py": 
        sys.exit("Not a Python file")
    else:
        print(get_length())

def get_length():
    try:
        with open(f"{sys.argv[1]}","r") as file:
            length = int(0)
            for line in file:
                if line.strip().startswith("#"):
                    pass
                elif line.strip()=="":
                    pass
                else:
                    length +=1 
            return length
    except FileNotFoundError:
        print("File can not open...")
        sys.exit()

if __name__ == "__main__":
    main()