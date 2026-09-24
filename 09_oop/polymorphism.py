# Polymorphism is a broad fundamental concept in object-oriented programming where a single 
# entity (like a variable, function, or object) can take many forms or exhibit different 
# behaviors depending on the context or object involved.

# In simpler words:
# Polymorphism allows different objects to respond to the same method or interface in their own way.


# 1. Built-in Function Polymorphism
# Python's built-in functions adapt their behavior based on the type of object passed to them. 
# A prime example is the len() function:
# # len() counts characters in a string
# print(len("Hello"))

# # len() counts elements in a list
# print(len([1, 2, 3]))



# 2. Operator Polymorphism (Operator Overloading)
# The same operator can perform different actions depending on the data types involved.
# Example:
# # Addition with numbers
# print(5 + 10)

# # Concatenation with strings
# print("Py" + "thon")



# 3. Polymorphism via Inheritance (Method Overriding)
# When a child class defines a method with the same name as a method in its parent class, 
# it "overrides" that behavior.
# It is used to implement one particular type of polymorphism (runtime or dynamic polymorphism).

# Example:
class Bird:
    def fly(self):
        print("All bird can fly.")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow fly high!")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly, they swim!")

# # Simply calling methods
# bird1 = Bird()
# bird1.fly()

# bird2 = Sparrow()
# bird2.fly()

# bird3 = Penguin()
# bird3.fly()

# Method overriding
birds = [Sparrow(), Penguin()]
for bird in birds:
    bird.fly()

# The loop doesn't need to know whether bird is a Sparrow or Penguin.
# It's doing "Method Overriding":
# The exact same function call (fly()) responds differently because the underlying 
# objects (sparrow vs penguin) are different.



# NOTE on Method Overloading:
# In languages like Java or C++, you can have multiple functions with the same name but different 
# signatures (different types or counts of arguments). Python does not support traditional method 
# overloading. If you define two methods with the same name, Python will simply overwrite the 
# first one with the last one defined.

# NOTE:
# Method overloading means writing multiple methods with the same name but different parameters 
# inside the same class, while method overriding means a child class redefines a method from its 
# parent class with the exact same signature.

# Method Overloading: Occurs within a single class without inheritance by using different parameters to achieve compile-time polymorphism. Return types may vary.
# Method Overriding: Requires inheritance between parent and child classes, maintaining identical parameters to achieve runtime polymorphism with matching or covariant return types.
