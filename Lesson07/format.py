import re
name = input("What is your name? ").strip().title()

if matches := re.search(r"^(.+), *(.+)$",name):
    last, first = matches.groups()
    name = f"{first} {last}"

print(f"hello, {name}")

