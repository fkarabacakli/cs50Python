def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
   
    number=int(0)
    char= int(0)
    finish = bool(False)
    s = s.strip()
    length = len(s)
    
                     
    for i in range(length):
        
        if finish == False:
            if s[i].isalpha()==True:
                char += 1
            elif s[i].isnumeric()==True:
                finish = True
                number += 1
                if s[i]=="0":
                    return False
            else:
                return False
                
        else:
            if s[i].isnumeric()==True:
                number +=1
            else:
                return False
        
    if char <2 or length>6 or length<2:
        return False

    return True

            
main()