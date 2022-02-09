#!/usr/bin/python3

class Person:
    def __init__(self, name, age):
       self.name = name
       self.age  = age

    def personDetails(self):
        print(self.name)
        print(self.age)


# person1 = Person("xyz", 10)
# person2 = Person("abc", 11)

# person1.personDetails()
# person2.personDetails()

class Parent(Person):
    def __init__(self, name, age, job):
        super().__init__(name,age)
        self.job = job
    
    def parentDetails(self):
        print(self.name)
        print(self.age)
        print(self.job)


parent1 = Parent("ashok,", 12, "swimmer")
parent1.parentDetails()

#test
