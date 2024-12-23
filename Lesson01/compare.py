def compare(x,y):
    
    if x>y :
        print(f"{x} is greater than {y}")
    elif y>x:
        print(f"{y} is greater than {x}") 
    else :
        print(f"{x} equal to {y}")    

    
def main():
    
    first  = int(input("What is the first number? "))
    second = int(input("What is the second number?"))
    compare(first,second)


main()
