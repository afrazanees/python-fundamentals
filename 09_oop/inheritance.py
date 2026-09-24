# Inheritance
# A class can inherit properties and methods from another class.
# The purpose of inheritance is to allow a class to reuse or extend behavior from another class.

# Example:

class Animal:
    def eat(self):
        print("Eating")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Dog(Animal):
    def bark(self):
        print("Barking")

dog = Dog()
dog.bark()           # own method
dog.eat()            # inherited
