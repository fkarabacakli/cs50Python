import emoji


while True:
    string = input("Input:")
    match string.strip().lower():
        case "exit" | "e":
            break
        case _:
            print(f"Output: {emoji.emojize(string,language='alias')}")