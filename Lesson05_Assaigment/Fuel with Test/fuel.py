import sys
def main():
    fuel = input("Input: ")
    pt = int(convert(fuel))
    print(gauge(pt))


def convert(fraction):
        x, y = fraction.strip().split("/")
        x = float(x)
        y = float(y)
        if y == 0:
            raise ZeroDivisionError
        elif x > y:
            raise ValueError
        return int(int(x) / int(y) * 100)

def gauge(percentage):

        if 0 <= percentage <= 1:
            return "EEE"
        elif 100 >= percentage >= 99:
            return "FFF"
        elif 1 < percentage < 99:
            return f"%{percentage}"
        else:
            raise TypeError


if __name__ == "__main__":
    main()
