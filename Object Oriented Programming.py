#Objects

print("Objects".upper())

s = "Apparently I'm just an object to you"
s2 = "I'm just another object"

print(s.upper())
print(s.count(" "))
print(s2.count(" "))

#Class

print("Class".upper())

from datetime import datetime

class Person:
    def __init__(self, name, dateofbirth):

        self.name = name
        self.birthdate = dateofbirth

        print("Hello")

    def get_age(self):

        today = datetime.now()
        b = datetime.strptime(self.birthdate, "%d/%m/%Y")
        age = today.year - b.year
        
        return age

groot = Person("I am Groot!", "04/05/2020")
ironman = Person("Tony Stark", "14/04/1990")

print(ironman.name)
print(ironman.birthdate)
print(ironman.get_age())

print(groot.name)
print(groot.birthdate)
print(groot.get_age())