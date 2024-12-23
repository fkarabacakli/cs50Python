class Student():
    def __init__(self,name,house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} lives in {self.house}"
    
    @classmethod
    def get(cls):
        while True:
            name = input("Name: ").strip().title()
            house = input("House: ").strip().title()
            if not name or not house:
                raise ValueError("Missing name or house.")
            else: 
                break
        return cls(name,house)

student = Student.get()
print(student)