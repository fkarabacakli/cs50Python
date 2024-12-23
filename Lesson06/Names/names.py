def in_list(file_name, name):
    with open(file_name, "r") as file:
        for line in file:
            if line == f"{name}\n":
                print("Give another name.")
                return True
        return False

def main():
    while True:
            name = input("What is your name? ")
            name = name.strip().title()
            if name == "":
                break
            elif in_list("names.txt", name):
                pass
            else:
                with open("names.txt", "a+") as out_file:
                    out_file.write(name)
                    out_file.write("\n")
    
    with open("names.txt") as file:
        for line in sorted(file,reverse=False):
            print(line.strip())


if __name__ == "__main__":
    main()