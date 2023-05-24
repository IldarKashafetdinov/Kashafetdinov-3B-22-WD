class GeometricFigure:
    def __init__(self, square, perimeter):
        self.square = square
        self.perimeter = perimeter


    def figure_info(self):
        print(f"площадь - {self.square}, периметр - {self.perimeter}")

fig = GeometricFigure(10, 20)

fig.figure_info()
