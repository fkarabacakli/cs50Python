def write(file_name):
    while True:
        name = input("What is your name: ").strip().title()
        if name.lower()=="" or name.lower()=="exit":
            break
        elif in_list("students.csv",name):
            pass
        else:
            city = input(f"Where do you live {name}? ").strip().title()
            number = get_phone_number()
            with open(file_name,"a+") as file:
                file.write(f"{name},{city},{number}\n")

def get_phone_number():
    while True:    
        s = str(input(f"What is your phone number?").strip())
        number= int(0) 
        for i in s:
            if i.isdigit()==True:
                number +=1
        
        if len(s)==0:
            if continue_process("Do you want to type phone number again? "):
                pass
            else:
                return "Unkown"
        elif s[0]!="+":
            print("Phone number must start with '+' !!!")
            if continue_process("Do you want to type phone number again? "):
                pass
            else:
                return "Unkown"
        elif number!=12:
            print("Invalid phone number!!!")
            if continue_process("Do you want to type phone number again? "):
                pass
            else:
                return "Unkown"
        else:
            counter = 0
            phone_number = ""
            for i in s:
                if i == "+" or i.isdigit()==True:
                    phone_number += i
                    counter += 1
                    if counter ==3 or counter==6 or counter==9:
                        phone_number += " "
                    
            return phone_number
    
def continue_process(s):
    answer = input(s)
    while True:
        match answer.strip().lower():
            case "yes" | "":
                return True
            case "no" | "exit":
                return False
            case _:
                print("Invalid command.. ",end="")


def in_list(file_name,check):
    with open(file_name)as file:
        for line in file:
            name,_,_=line.split(",")
            if name==check.strip().title():
                print("List has same name!!!")
                if continue_process("Do you want to add same name again? "):
                    return False
                else:
                    return True
        return False
    

def read(line):
    name , city , phone_number = line.strip().split(",")
    student = {"name":name,"city":city,"phone_number":phone_number}
    return student

def main():
    students = []
    write("students.csv")
    if continue_process("Do you want to print data? "):
        
        with open("students.csv") as file:
            for line in file:
                students.append(read(line))
        
        for student in sorted(students, key=lambda student:student["name"] , reverse=False):
            print(f"{student['name']} lives in {student['city']} and phone number is {student['phone_number']}.")
    else:
        pass


if __name__ == "__main__":
    main()