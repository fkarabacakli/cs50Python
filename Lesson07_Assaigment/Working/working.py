import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = "(0?[1-9]|1[0-2]):?([0-5][0-9])? (am|pm)"
    match = re.search(r"^" + regex + " to " + regex + "$", s)
    if match:
        start_hour = int(match.group(1))
        end_hour = int(match.group(4))
        
        if match.group(2)!=None:
            start_minute = match.group(2)
        else:
            start_minute = int(0)
        
        if match.group(5)!=None:
            end_minute = match.group(5)
        else:
            end_minute = int(0)

        if match.group(3)=="pm":
            start_hour += 12
        if match.group(6)=="pm":
            end_hour +=12

        return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"
    else:
        sys.exit("Invalid command type...")



if __name__ == "__main__":
    main()   