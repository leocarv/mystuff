# -*- coding: utf-8 -*-
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Make a class named Dog that is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## From self get the name attribute and set it to parameter name
        self.name = name

## Make a class named Cat that is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## From self get the name attribute and set it to parameter name
        self.name = name

## Make a class named Person that is-a object
class Person(object):

    def __init__(self, name):
        ## From self get the name attribute and set it to parameter name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Make a class named Employee that is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## From self get the salary attribute and set it to parameter salary
        self.salary = salary

## Make a class named Fish that is-a object
class Fish(object):
    pass

## Make a class named Salmon that is-a Fish
class Salmon(Fish):
    pass

## Make a class named Halibut that is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## From mary get the pet attribute and set it to satan
mary.pet = satan

## Set frank to an instance of class Employee
frank = Employee("Frank", 120000)

## From mary get the pet attribute and set it to satan
frank.pet = rover

## Set flipper to an instance of class Fish
flipper = Fish()

## Set flipper to an instance of class Fish
crouse = Salmon()

## Set harry to an instance of class Halibut
harry = Halibut()