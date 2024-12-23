import csv
import sys
from tabulate import tabulate

tables=[]
length = len(sys.argv)

if length<2:
    sys.exit("Too few command-line arguments")
elif length>2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:]!=".csv":
    sys.exit("Invalid file type..")

try:
    with open(f"{sys.argv[1]}") as file:
        reader = csv.reader(file)
        for row in reader:
            tables.append([row[0],row[1],row[2]])
    print(tabulate(tables[1:],headers=tables[0],tablefmt="grid"))
except FileExistsError:
    sys.exit("File could not open...")



