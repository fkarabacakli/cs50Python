def check(w):
    if len(w.split()) != 3:
        print("Invalid command...")
        return False
    x,y,z = w.split()
    if x.isnumeric()==False or z.isnumeric()==False:
        print("Give integer")
        return False
    elif possible(y)==False:
        print("You can not do this ")
        return False
    else:
        return True
    
def possible(char):
    char = char.strip()
    match char:
        case "+"|"-"|"/"|"*"|"%":
            return True
        case _:
            return False

def new_math():
    while True:
        k = input("İşlem yapmak ister misin? (Yes/No)")
        k = k.lower().strip()
    
        match k:
            case "yes":
                return True
            case "no"| "exit":
                return False
    
def math(s):
    
    x,y,z = s.split()
    x = float(x)
    z = float(z)
    
    match y:
        case "+":
            print(x+z)
        case "-":
            print(x-z)
        case "*":
            print(x*z)
        case "/":
            print(x/z)
        case "%":
            print(x%z)

def islem():
    while True:
                words = input("What is the question => ")
                match words:
                    case "exit":
                        return False
                    
                if check(words)== True:
                    math(words)
                    return True
    
                else:
                    print("Give new command ",end="")
    
def main():
    while True:
        if new_math()==True:
            if islem()==False:
                return False
        else :
            return False
        

main()
