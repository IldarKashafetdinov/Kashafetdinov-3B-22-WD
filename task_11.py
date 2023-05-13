class Dog:

    def __init__(self, name, breed ,age):
        self.name = name
        self.breed = breed
        self.age = age

    def about_dog(self):
        print(f"{self.breed} по кличке - {self.name}, которой {self.age}")


dog = Dog("Шарик", "Такса", 3)
dog.about_dog()