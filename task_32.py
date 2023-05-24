class Student:
    def __init__(self, name, clas):
        self.name = name
        self.clas = clas

    def study(self):
        print(f"{self.name} учится в {self.clas} классе")


Student1 = Student("Ильдар", 1)

Student1.study()
