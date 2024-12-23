students = [
    {"name":"Furkan", "house":"Denizli"},
    {"name":"Semih", "house":"Kütahya"},
    {"name":"Ayperi", "house":"Kütahya"},
    {"name":"Can", "house":"Mugla"},
    {"name":"Adem", "house":"Kütahya"},
    {"name":"Nihat", "house":"Izmir"},
]

def main_v1():
    def is_kütahya(s):
        if s["house"]=="Kütahya":
            return True
        else:
            return False
        
    def sorting(s):
        return s["name"]
        
        
    kütahyalilar = filter(is_kütahya, students)
    for kütahyali in sorted(kütahyalilar, key=sorting):
        print(kütahyali["name"])

def main_v2():
    
    kütahyalilar = filter(lambda s : s["house"]=="Kütahya", students)
    for kütahyali in sorted(kütahyalilar, key=lambda s: s["name"]):
        print(kütahyali["name"])
    
main_v2()