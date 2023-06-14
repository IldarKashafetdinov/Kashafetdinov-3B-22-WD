class ProductCard:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty


    def reduction_qty(self, index):
        self.qty -= index
        if self.qty > 0:
            self.qty = self.qty
        else:
            self.qty = "Товар закончился"



    def change_price(self, plus, index):
        if plus == True:
            self.price += index
        else:
            self.price -= index
            if self.price > 0:
                self.price = self.price
            else:
                self.price = "Цена товара не может быть отрицательной"


    def print(self):
        print(f"Название товара - {self.name}\nЦена - {self.price}\nКоличество - {self.qty}")


milk = ProductCard('milk', 120, 6)
milk.reduction_qty(7)
milk.change_price(True, 300)
milk.print()
