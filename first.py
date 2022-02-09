#!/usr/bin/python3

class Person:
    def __init__(self, name, age):
       self.name = name
       self.age  = age

    def personDetails(self):
        print(self.name)
        print(self.age)


person1 = Person("xyz", 10)
person2 = Person("abc", 11)

person1.personDetails()
person2.personDetails()




