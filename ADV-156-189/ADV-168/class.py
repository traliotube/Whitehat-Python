class Citizen:
    def __init__(self, name, age, dob, id):
        self.name = name
        self.age = age
        self.dob = dob
        self.id = id

    def addCitizen(self):
        print("Adding Citizen...")
        print("Name: ", self.name)
        print("Age: ", str(self.age))
        print("DOB: ", self.dob)
        print("ID: ", int(self.id))


citizen1 = Citizen("Peter", 8, "19th Oct 2012", 198)
citizen1.addCitizen()
citizen2 = Citizen("Sophia", 10, "19th Oct 2010", 199)
citizen2.addCitizen()
