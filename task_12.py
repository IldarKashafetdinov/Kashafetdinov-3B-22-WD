class Student:

    def __init__(self, name, surname, cours, grades):
        self.name = name
        self.surname = surname
        self.cours = cours
        self.grades = grades
    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Ildar", "Kash", 1, [1, 2, 3, 4, 5])
print(f"{student.name} {student.surname}, {student.cours} курс, средний бал - {student.average_grade()}")