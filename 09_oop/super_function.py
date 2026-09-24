# super()
# super() allows a child class to access methods or initialization logic from its parent class.
# Used as super().__init__() or super().method_name() to call parent methods through a temporary proxy object.

# NOTE:
# super() is a Python tool used to implement inheritance, which establishes an "Is-A" relationship 
# (e.g., a Car is a Vehicle) by allowing a child class to cleanly trigger and reuse its parent's 
# code. This is fundamentally different from composition, which defines a "Has-A" relationship 
# (e.g., a Car has an Engine) by plugging smaller, independent objects together as attributes 
# rather than inheriting their traits.

# Example:

# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
#         print(f"{self.name} is of {self.breed} breed.")

# my_dog = Dog("ABC", "XYZ")
