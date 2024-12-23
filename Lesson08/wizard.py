class Wizard:
    def __init__ (self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

    def __str__(self) -> str:
        return self.name

class Student(Wizard):
    def __init__ (self, name, house):
        super().__init__(name)
        self.house = house
    
    def __str__(self) -> str:
        return f"{self.name} lives in {self.house}"

class Professor(Wizard):
    def __init__ (self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    def __str__(self) -> str:
        return f"{self.name} professor of {self.subject} lesson."
    
wizard = Wizard(input("Name: ").strip().title())
student = Student("Furkan", "Denizli")
professor = Professor("David", "Introduction to Computer Science")

print(wizard)
print(student)
print(professor)
