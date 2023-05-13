class Book:

    def __init__(self, name, author, yearOfRelease, genre):
        self.name = name
        self.author = author
        self.yearOfRelease = yearOfRelease
        self.genre = genre

    def getBookInfo(self):
        print(f"{self.name}, {self.author} ({self.yearOfRelease}), {self.genre}")
