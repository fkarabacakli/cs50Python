students = [
    {"name":"Semih", "house":"Kütahya"},
    {"name":"Adem", "house":"Kütahya"},
    {"name":"Nihat", "house":"Izmir"},
    {"name":"Can", "house":"Mugla"},
    {"name":"Furkan", "house":"Denizli"},
]

houses = set()

for student in students:
    if student["house"] not in houses:
        houses.add(student["house"])

for house in sorted(houses):
    print(house)