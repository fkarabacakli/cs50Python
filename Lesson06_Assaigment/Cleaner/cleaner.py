import csv
import sys

length = len(sys.argv)

if length < 3:
    sys.exit("Too few command-line arguments")
elif length > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:] != ".csv" or sys.argv[2][-4:] != ".csv":
    sys.exit("Invalid file type...")


people = []

try:
    with open(f"{sys.argv[1]}") as file:
        reader = csv.DictReader(file)
        file.fieldnames = ["name", "house"]
        for row in reader:
            people.append({"name": row["name"], "house": row["house"]})
except FileNotFoundError:
    sys.exit("File could not found...")


try:
    with open(f"{sys.argv[2]}", "w") as file:
        writer = csv.DictWriter(file, fieldnames={"first_name", "second_name", "house"})
        writer.writeheader()

        for person in sorted(people, key=lambda person: person["name"]):
            first_name, second_name = person["name"].split(",")
            house = person["house"]
            file.write(f"{first_name.strip()},{second_name.strip()},{house.strip()}\n")
except FileExistsError:
    sys.exit("File could not create...")
