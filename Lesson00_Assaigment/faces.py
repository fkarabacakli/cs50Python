def main():
    s = input()
    print(convert(s))


def convert(a):
    a = a.replace(":)","😐")
    a = a.replace(":(","🙁")
    return a

main()


