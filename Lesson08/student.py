
class Student_Information:
    def __init__(self):
        self.name     = input("Name : ").strip().title()
        self.house    = input("House: ").strip().title()
    
    def __str__(self):
        return f"{self.name} is from {self.house}"
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name...")
        self._name = name
 
    @property
    def house(self):
        return self._house
    @house.setter
    def house(self, house):
        if house not in ["Kale", "Denizli","Osmaniye"]:
            raise ValueError("Missing House...")
        self._house = house
        
def main():
    student = Student_Information()
    print(student)


        

if __name__ == "__main__":
    main()
