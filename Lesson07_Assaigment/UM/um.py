import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(s):
    data_type = r"(\W|^)um(\W|$)"
    match = re.findall(data_type ,s,re.IGNORECASE)
    return len(match)


if __name__ == "__main__":
    main()