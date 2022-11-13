class Book:
    def __init__(self, name, author, price, yearOfPublishing):
        self.name = name
        self.author = author
        self.price = price
        self.year = yearOfPublishing

    def addBook(self):
        print("Adding Citizen...")
        print("Name: ", self.name)
        print("Author: ", str(self.author))
        print("Price: ", self.price)
        print("Year of publishing: ", int(self.year))

    def yearsSincePublished(self):
        print(
            f"This book was published on {self.year} which was {2022 - self.year} years ago")


book1 = Book("Harry Potter and the Philosopher's Stone",
             "J.K. Rowling", 1928, 1997)
book1.addBook()
book1.yearsSincePublished()
book2 = Book("Diary of a Wizard", "Jeff Kinney", 700, 2017)
book2.addBook()
book2.yearsSincePublished()
