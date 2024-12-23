
greet = input("Greeting: ")
match greet:
    case "hello":
        print("$0")
    case _:
        if greet[0]=="h":
            print("$20")
        else:
            print("$100")