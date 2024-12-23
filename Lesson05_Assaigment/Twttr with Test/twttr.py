def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]

    # save output like an array
    str1 = ""
    for i in word:
        if i.lower() not in vowels:
            str1 += i
    return str1


if __name__ == "__main__":
    main()
