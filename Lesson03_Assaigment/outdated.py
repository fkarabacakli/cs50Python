
def outdated():
    months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]
   
    while True:
        try:
            string = str(input("Date: "))
            if "/"in string:
                
                mm,dd,yyyy =string.split("/")
                mm=int(mm.strip())
                break
                
            elif "," in string:
                    
                    mmdd,yyyy = string.split(",")
                    mmdd= mmdd.strip()
                    mm,dd = mmdd.split(" ")
                    mm=int(months.index(mm.title().strip())+1)
                    break
                
        except ValueError:
            print("Uncorrect usage..")
    
    dd=int(dd.strip())
    yyyy=int(yyyy.strip())
    
    if mm>12 or dd>31:
        print("Invalid dates...")
    
    print(yyyy,end="/")
    print(f"{mm:02}",end="/")
    print(f"{dd:02}")        
    
def main():
     while True:
              if outdated()==True:
                   return True




    
    

main()
