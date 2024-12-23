import csv

def get_input():
    while True:
        if continue_process("Do you want to add new person? "):
            user_name = input("What is your name? ").strip().title()
            user_city = input("Where do yo live? ").strip().title()
            user_phone_number = get_phone_number()
            if in_list("students.csv",user_phone_number,"phone_number"):
                print("You cant add this person because there is another person in the list, who is have same phone number..")
                pass
            else:
                write(user_name,user_city,user_phone_number)
        else:
            return False


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


def in_list(file_name,check_word,kind):
    with open(file_name)as file:
        if check_word == "Unkown":
            return False
        reader = csv.DictReader(file)
        for row in reader:
            if row[kind]==check_word:
                return True
        return False


def write(name,city,phone_number):
    with open("students.csv", "a+") as file:
        writer = csv.DictWriter(file,fieldnames=["name","city","phone_number"])
        writer.writerow({"name":name,"city":city,"phone_number":phone_number})


def continue_process(s):
    while True:
        answer = input(s)
        match answer.strip().lower():
            case "yes" | "" :
                return True
            case "no" | "exit":
                return False
            case _:
                print("Invalid command.. ",end="")


def read():
    students = []
    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name":row['name'],"city":row['city'],"phone_number":row['phone_number']})
    
    for student in students:
        print(student['name'],student['city'],student['phone_number'],sep=" / ")

def read_names():
    students = []
    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name":row['name']})
    
    for student in students:
        print(student['name'],sep=" / ")


def start():
    while True:
        print("----------------------------------")
        print("1)Add new person to list\n2)Print all information\n3)Print only names in the list")
        print("----------------------------------")
        answer = input("Which function would you like to do? ").strip()
        if answer.lower() == "exit":
            return 0
        elif answer.isnumeric()==True:
            answer = int(answer)
            if 0<answer<4:
                return answer
    
        print("Invalid command...")


def main():
    while True:
        function = start()
        if function==0:
            break
        elif function==1:
            get_input()
            if continue_process("Do you want to do another function? ")==False:
                break
        elif function==2:
            read()
            if continue_process("Do you want to do another function? ")==False:
                break
        elif function==3:
            read_names()
            if continue_process("Do you want to do another function? ")==False:
                break
        else:
            print("Function error!!!")
            break

    
if __name__ == "__main__":
    main()