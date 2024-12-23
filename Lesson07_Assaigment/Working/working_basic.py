import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    start,end = s.strip().lower().split("to")
    if ":" in start and ":" in end:
        
        start_time,start_ampm = start.strip().split(" ")
        start_hour,start_minute = start_time.strip().split(":")
        start_hour,start_minute = int(start_hour),int(start_minute)

        end_time,end_ampm = end.strip().split(" ")
        end_hour,end_minute = end_time.strip().split(":")
        end_hour,end_minute = int(end_hour),int(end_minute)
        
        if start_hour>12 or start_minute>60 or end_hour>12 or end_minute>60:
            sys.exit("Invalid")
             
        if start_ampm.lower()=="pm":
            start_hour+=12
        if end_ampm.lower()=="pm":
            end_hour+=12
        
        return f"{start_hour}:{start_minute} to {end_hour}:{end_minute}"
    else:
        start_time,start_ampm = start.strip().split(" ")
        start_time = int(start_time)

        end_time,end_ampm = end.strip().split(" ")
        end_time = int(end_time)

        if start_time>12 or end_time>12:
            sys.exit("Invalid command")
        
        if start_ampm.lower()=="pm":
            start_time +=12
        if end_ampm.lower()=="pm":
            end_time+=12
        
        return f"{start_time} to {end_time}"
        



if __name__ == "__main__":
    main()