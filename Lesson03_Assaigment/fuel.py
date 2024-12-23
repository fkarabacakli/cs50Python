def fuel_information():
    while True:
        try:
            s = input("Fraction :").strip()
            x,y=s.split("/")
            x=float(x.strip())
            y=float(y.strip())
            z=(x/y)*100
            return int(z)
        except  (ValueError, ZeroDivisionError):
            print("Usage: x/y ")

def main():
    percentage = fuel_information()
    if percentage>=99:
        print("F")
    elif percentage<=1:
        print("E")
    else:
        print(f"%{percentage}")

main()