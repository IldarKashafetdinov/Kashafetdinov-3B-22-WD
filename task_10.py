class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about_person(self):
        print("Имя: " + self.name)
        print("Возраст: " + str(self.age))


pers = Person("Alex", 18)
pers.about_person()

