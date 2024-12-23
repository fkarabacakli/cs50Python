def camel_print(s):
    print("snake_case : ",end="")
    
    for i in s:
        if i.isupper()== True:
            print("_",i.lower(),end="",sep="")
        else:
            print(i,end="")
    print()

def main():
    string = str(input("Camel Case: ")).strip()
    camel_print(string)

main()