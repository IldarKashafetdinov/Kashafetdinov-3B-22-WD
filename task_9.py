class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def square(self):
        res = self.width * self.length
        return f"Площадь прямоугольника шириной {self.width} и длинной {self.length} равна: {res}"


rect1 = Rectangle(3, 6)
rect2 = Rectangle(100, 4)
print(rect1.square())
print(rect2.square())

