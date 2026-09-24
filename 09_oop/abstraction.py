# Abstraction means hiding the intricate inner workings of a system and only exposing a clean, 
# high-level interface. The user knows how to interact with the component but does not need to 
# understand how its methods are written under the hood.

# In Python, this is formally implemented using the abc (Abstract Base Class) module. 
# You define a blueprint that enforces what methods a subclass must have, 
# without implementing them in the parent.

# Example:
from abc import ABC, abstractmethod     # abc means "Abstract Base Class"

# Abstract Base Class acting as a strict template
class Vehicle(ABC): # To make a class an 'abstract base class', inherit from ABC.

    # The @abstractmethod decorator marks a method as a blueprint that child classes must override and implement.
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle): # Inherit from the base class Vehicle
    def start_engine(self):
        # The user just calls start_engine(), ignoring the internal mechanics below
        return "Ignition turned on, fuel injected, pistons moving."

class ElectricScooter(Vehicle):
    def start_engine(self):
        return "Battery activated, system boot complete."

my_car = Car()
print(my_car.start_engine())
