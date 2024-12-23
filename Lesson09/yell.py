def main():
    yell_v2("This", "is", "CS", "50")

def yell_v1(*words):
    output = map(str.upper,words)
    print(*output)

def yell_v2(*words):
    output = [word.upper() for word in words]
    print(*output)

if __name__ == "__main__":
    main()