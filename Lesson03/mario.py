
def main():
    while True:
        choce = input("Which fuction would you like to use? (while/recursion) ")
        match choce.strip().lower():
            case "while":
                height = get_int("What is the height? ")
                draw(height)
                return True
            case "recursion":
                height = get_int("What is the height? ")
                drawv2(height,height)
                return True
            case _:
                print("Only you can 'while' and 'recursion' functions...")


def get_int(s):
    while True:
        try:
            i = int((input(s)))
            return i
        except ValueError:
            print("It must be integer...")

def draw(height):

    while True:
        for i in range(height):
            new = height-i+1
            print(" "*new,end="")
            print("#"*(i+1)*2)

        return True
    
def drawv2(height,sharp):

    if height==0:
        return
    
    drawv2(height-1,sharp)
    
    n = sharp-height
    print(" "*n,end="")
    print("#"*height,end=" ")
    print("#"*height)

        

main()