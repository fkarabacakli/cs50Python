from validator_collection import checkers

def main():
    print(check(input("E-Mail: ").strip()))

def check(s):
    if checkers.is_email(s)==True:
        return "Valid"
    else:
        return "Invalid"
    
if __name__ == "__main__":
    main()

