class Student:

    def __init__(self, name, surname, age, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.profession = profession

    def student_info(self):
        print(f"{self.name} {self.surname}, {self.age}, {self.profession}")

