def main():
    string = input("Input: ")
    print(value(string))


def value(greeting):
    greeting = greeting.strip().lower()
    match greeting:
        case "hello":
            return int(0)
        case _:
            if greeting[0]=="h":
                return int(20)
            else:
                return int(100)


if __name__ == "__main__":
    main()