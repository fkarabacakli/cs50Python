students = [
    {"name": "Furkan", "house": "Denizli"},
    {"name": "Semih", "house": "Kütahya"},
    {"name": "Ayperi", "house": "Kütahya"},
    {"name": "Can", "house": "Mugla"},
    {"name": "Adem", "house": "Kütahya"},
    {"name": "Nihat", "house": "Izmir"},
]

kütahyalilar = [
    student["name"] for student in students if student["house"] == "Kütahya"
]

print(*sorted(kütahyalilar), sep=", ")
