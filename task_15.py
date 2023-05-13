class Car:

    def __init__(self, brand, model, year_issue, price):
        self.brand = brand
        self.model = model
        self.year_issue = year_issue
        self.price = price

    def car_info(self):
        print(f"{self.brand} - {self.model}, {self.year_issue}, {self.price}")

