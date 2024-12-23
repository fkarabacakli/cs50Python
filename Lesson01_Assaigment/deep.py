def main():
    name = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    
    match name:
        case "forty two" | "forty-two" | "42":
            print("Yes")
        case _:
            print("No")    

main()