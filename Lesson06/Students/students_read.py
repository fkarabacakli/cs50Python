import csv
students = []
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name":row['name'],"city":row['city'],"phone_number":row['phone_number']})
    
for student in students:
    print(student['name'],student['city'],student['phone_number'],sep=" / ")