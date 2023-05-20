class Worker:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def worker_info(self):
        print(f"Имя - {self.name} \nВозраст - {self.age} \nЗ/П - {self.salary}$")

worker1 = Worker("Alex", 23, 1000)

worker1.worker_info()
