def main():
    number = int(input("What is the number? "))

    if is_even(number):
        print("Eveen")
    else:
        print("Odd")

def is_even(i):
    return i%2==0 
    
main()    
