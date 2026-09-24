# IS-A Relationship (Inheritance)
# A subclass (child class) is a specialized version of a superclass which extends the behavior of the superclass (parent class).
# Changes to the parent class can directly affect child behavior.
# Real-World Example: A Car is a Vehicle.
# Example:

# class Vehicle:
#     def __init__(self, brand):
#         print(f"Car brand is {brand}")

#     def move(self):
#         print("Moving down the road.")

# class Car(Vehicle):
#     def honk(self):
#         print("Beep Beep!")

# car = Car("ABC")
# car.move()
# car.honk()



# HAS-A Relationship (Composition)
# A class uses another class as an internal component.
# Components can be easily swapped or modified independently.
# Real-World Example: A Car has an Engine.
# Example:
# class Engine:
#     def start(self):
#         return "Engine vrooms!"

# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#         self.engine = Engine()

#     def start(self):
#         print(f"{self.brand} is ready. {self.engine.start()}")

# my_car = Car("ABC")
# my_car.start()




# Q. When would you use inheritance versus composition?

# Use inheritance when there is a genuine 'is-a' relationship and the child should share or extend the parent's behavior. 
# Use composition when one object needs to contain or use another object. Composition can often provide more flexibility and looser coupling.
