def main():
    clock = input("What time is it? ")
    clock = convert(clock)

    if clock >= 18.00 and clock <= 19.00:
        print("Dinner Time")
    elif clock >= 12.00 and clock <= 13.00:
        print("Lunh Time")
    elif clock >= 7.00 and clock <= 8.00:
        print("Breakfast Time")
    elif clock ==False:
        print("Uncorrect Usage") 
    else:
        print("Do whatever you want..")    

    
def convert(time):
    x,y = time.split(" ")
    hour,minute = x.split(":")
    minute = float(minute)/60
    match y:
        case "a.m.":
            return float(hour)+minute
        case "p.m.":
            return float(hour)+minute +12.00
        case _:
            return False
       
    


if __name__ == "__main__":
    main()