from sys import exit
import re

email = input("What is your e-mail adress? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|net|org)$", email, re.IGNORECASE):
    print("Valid")
else: 
    print("Invalid")