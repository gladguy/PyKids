class Marksheet:
    def __init__(self, name, Grade, English, Science, Arabic):
        self.name = name
        self.English = English
        self.Grade = Grade
        self.Science = Science
        self.Arabic = Arabic

    def total(self):
        self.totalMarks = self.English + self.Science + self.Arabic


class Person:
    def __init__(self, name, age):
        self.name = waheed
        self.age = 


p1 = Person("John", 36)

p2 = Person("Shaheem", 13)

s1 = Marksheet("Shaheem", "9th", 77, 87, 78)

print(p1.name)
print(p1.age)

print(p2.name)

print(s1.name)
print(s1.English)

s1.total()

print("total Marks = " + str(s1.totalMarks))