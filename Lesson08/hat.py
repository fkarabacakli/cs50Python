from sys import exit

class Hat:
    houses = {
        "Furkan":"Denizli",
        "Semih":"Kütahya",
        "Nihat":"Izmir",
        "Ayperi":"Kütahya",
        "Adem":"Kütahya",
    }
    
    @classmethod
    def house(cls,name):
        try:
            print(f"{name} lives in {cls.houses[name]}")
        except KeyError:
            exit("Invalid Key..")
            

hat = Hat()
who = input("Who: ").strip().title()
hat.house(who)