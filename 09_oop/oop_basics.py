# Class - Blueprint/template for creating Objects. It defines "attributes and methods" for an Object.
# class User:
#     # Class attributes and methods here
#     print("Hello")
#     def hello(self):
#         print("World")



# Object
# The actual structure/instance built from that blueprint/template (which is "Class").
# In programming, "an object is any real-world entity". But Python follows the philosophy:
# "Everything is an Object". So for Python, an Object can be described as:
# "An Object represents any real-world entity or a concept in a program".
# An Object contains "data/attributes and behaviors/methods". It contains its own data/attributes
# and uses the methods defined by the class.
# user1 = User()
# user1.hello()



# Instance Attributes - These belong to individual objects.
# class User:
#     def __init__(self, name):
#         self.name = name
# # Each object has its own. Changing one doesn't normally change the other.
# user1 = User("Ali")
# user2 = User("Sara")



# Class Attributes - A class attribute belongs to the class and can be shared by instances.
# class User:
#     role = "user"

#     def __init__(self):
#         pass

# user1 = User()
# user2 = User()
# # Both can access:
# print(user1.role)
# print(user2.role)



# "Methods" OR "Instance Methods" - A function defined inside a class.
# class User:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, {self.name}")



# __init__ 
# It is an initializer method that automatically runs when an object is created. In other words, 
# you don't have to call this method for it to run. 
# NOTE: 
# __init__ acts as the constructor in Python for all practical purposes, though technically 
# speaking, it is an initializer rather than a creator.
# When you instantiate a class in Python, the object-creation process is split into two distinct steps:
# 1. Object Creation (__new__): Python first calls the __new__ method to physically allocate memory and create the raw, blank object.
# 2. Initialization (__init__): Once the object is created, Python automatically hands that blank object over to the __init__ method. 
#                               The __init__ method then initializes the object's starting state by assigning properties and attributes.
# Because __init__ is where you define parameters and set up your initial data, the Python community universally refers to it as the class constructor.
# class User:
#     def __init__(self, name):
#         self.name = {name}
#         print(f"Hello {name}")

# user1 = User("ABC")
# It's commonly used to initialize the object's attributes.




# self Keyword
# It's passed as a first parameter to every method of a class, and can be used inside the methods.
# i.e., 
# class User:
#     def __init__(self):
#         pass

#     def set_name(self, name):
#         self.name = name

# When calling any particular method from a class, it does not require self to be passed explicitly as an argument.
# i.e.,
# user1 = User()
# # Here, we are not passing self as an argument even though self is defined as a parameter in the methods of the class.
# user1.set_name("ABC")
# Under the hood, Python automatically passes the object as that argument when you call the method.
# i.e.,
# For user1.set_name("ABC"), Python interprets this as User.set_name(user1, "ABC")

# In simpler words, 
# self -> this instance of the class
# This is because a class can have multiple instances, and every instance shares the same template/blueprint
# of the class. So whenever we call a method for any instance, something like:
# user1.set_name("ABC")
# user2.set_name("XYZ")
# the class needs to know which instance you are referring to, so that it can apply the called method
# to the right instance (object) of the class.
# i.e.,
# user1.set_name("ABC")
# In the above example, "user1" is exactly the same thing as "self". So whenever I call a method of that
# "user1 instance", this "user1" is passed as the first argument (under the hood in Python).
# To verify it:
# class Player:
#     def play(self, var):
#         print(self, var)

# player1 = Player()
# player1.play(player1)
# In the above example, to verify that 'self' and 'player1' are the same thing, we passed 'player1'
# as the first argument and printed the location of "self" and "player1" in memory.
# Both point to the exact same memory location.
# NOTE:
# "self" is just a convention and not a reserved keyword in Python. You can change it to
# whatever you want, but using "self" is the best practice as it is recognized universally by
# the Python community.




# OOP example
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello! My name is {self.name}. I am {self.age} old.")

student1 = student("ABC", 10)
student2 = student("XYZ", 12)

student1.introduce()
student2.introduce()
