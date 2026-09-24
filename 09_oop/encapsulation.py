# Encapsulation wraps data (attributes) and behavior (methods) into a single unit (a class) and 
# restricts direct external access to prevent accidental modification.
# Its main goal is to "Protect internal state and data integrity from outside interference".
# In different programming languages, it is done using keywords like "private" or "public" (e.g., C++).
# In Python, there are no strict access modifier keywords.
# Python enforces encapsulation largely by convention using underscores:
# 1. self.variable: Accessible from anywhere (inside or outside the class).
# 2. self._variable: Protected (a convention indicating internal use; not to touch outside the class). 
# 3. self.__variable: Private (triggers name mangling, making it harder to access directly).

# NOTE on "NAME MANGLING": 
# Name mangling is a programming technique where compilers or interpreters automatically change the
# original name of a variable, function, or class into a new, unique internal name.
# In Python, starting a class attribute or method with two underscores (__name) triggers automatic name mangling.
# Python changes the name internally to _ClassName__name (for example, __balance in a class named "Account" becomes _Account__balance).
# This prevents a subclass from accidentally overwriting methods or variables defined in a parent class. 
# It is not meant for true data privacy or security.

# Example:

# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount

#     def get_balance(self):
#         print(f"Balance is {self._balance}")

# user1 = BankAccount(1000)
# user1.get_balance()
# user1.deposit(500)
# user1.get_balance()

# # Now in the above example, we have "protected only" the "balance" attribute.
# # But it's not private, so the user can access and manipulate it directly.
# # To verify it:
# print(user1._balance)           # This will give balance amount directly
# user1._balance = 10000          # And user can manipulate it directly.
# print(user1._balance)           

# To restrict its access (encapsulation), and to avoid direct manipulation of attributes:
class newBankBalance:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def getBalance(self):
        print(f"Balance is {self.__balance}")

user1 = newBankBalance(1000)
user1.getBalance()
print(user1.__balance)              # This will throw an AttributeError, because of "Name Mangling"
# Name Mangling changes the internal name of __balance to _newBankBalance__balance
# print(user1._newBankBalance__balance)


# Instead of letting external code change variables directly, encapsulation uses 
# Getter and Setter methods to safely view and update private data.
