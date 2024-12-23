import sys
import re

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    value_type = "([1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
    match = re.search(r"^"+ value_type + ":" + value_type + ":" + value_type + ":" +  value_type +"$" ,ip)
    if match:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
