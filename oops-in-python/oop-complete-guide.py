# ============================================================
# OOP IN PYTHON — COMPLETE GUIDE
# ============================================================


# ------------------------------------------------------------
# 1. CLASS AND OBJECT
# ------------------------------------------------------------
# A class is a blueprint. An object is a thing built from it.

class Car:
    pass

car1 = Car()
car2 = Car()
print("1. Class & Object:", car1, car2)


# ------------------------------------------------------------
# 2. __init__ AND INSTANCE ATTRIBUTES
# ------------------------------------------------------------
# __init__ runs automatically when you create an object.
# self refers to the object being built.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Daniel", 35)
print("2. Instance attributes:", p1.name, p1.age)


# ------------------------------------------------------------
# 3. CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES
# ------------------------------------------------------------
# Class attributes are shared by ALL instances.
# Instance attributes belong to ONE specific object.

class Employee:
    company = "WBA"  # class attribute (shared)

    def __init__(self, name):
        self.name = name  # instance attribute (unique)

e1 = Employee("Zain")
e2 = Employee("Naren")
print("3. Class attr:", e1.company, "==", e2.company)
print("   Instance attr:", e1.name, "vs", e2.name)


# ------------------------------------------------------------
# 4. METHODS — INSTANCE, CLASS, STATIC
# ------------------------------------------------------------

class Calculator:
    version = "1.0"

    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):                 # instance method - uses self
        print(f"   Brand: {self.brand}")

    @classmethod
    def show_version(cls):                # class method - uses cls
        print(f"   Version: {cls.version}")

    @staticmethod
    def add(a, b):                        # static method - no self/cls
        return a + b

calc = Calculator("Casio")
print("4. Methods:")
calc.show_brand()
Calculator.show_version()
print("   2 + 3 =", Calculator.add(2, 3))


# ------------------------------------------------------------
# 5. ENCAPSULATION (hiding data)
# ------------------------------------------------------------
# _name = "protected" by convention (don't touch from outside)
# __name = "private" (Python mangles the name to prevent access)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount("Daniel", 1000)
acc.deposit(500)
print("5. Encapsulation: balance =", acc.get_balance())
# print(acc.__balance)  <- would crash. Has to go through get_balance().


# ------------------------------------------------------------
# 6. INHERITANCE (one class extends another)
# ------------------------------------------------------------

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"   {self.name} makes a sound.")

class Dog(Animal):                # Dog inherits from Animal
    def speak(self):              # override the parent method
        print(f"   {self.name} says Woof!")

class Puppy(Dog):                 # Puppy inherits from Dog
    def speak(self):
        super().speak()           # call parent version first
        print(f"   {self.name} also wags tail.")

print("6. Inheritance:")
Animal("Generic").speak()
Dog("Rex").speak()
Puppy("Buddy").speak()


# ------------------------------------------------------------
# 7. POLYMORPHISM (same method name, different behaviour)
# ------------------------------------------------------------
# You can treat different objects the same way if they share
# a method name. Python doesn't care about the type.

class Cat:
    def speak(self):
        print("   Meow")

class Cow:
    def speak(self):
        print("   Moo")

print("7. Polymorphism:")
for animal in [Dog("Rex"), Cat(), Cow()]:
    animal.speak()


# ------------------------------------------------------------
# 8. ABSTRACTION (force subclasses to implement methods)
# ------------------------------------------------------------
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

print("8. Abstraction:")
print("   Square area:", Square(4).area())
print("   Circle area:", Circle(3).area())
# Shape()  <- would crash. Can't create an abstract class directly.


# ------------------------------------------------------------
# 9. DUNDER METHODS (__str__, __repr__, __len__, __eq__)
# ------------------------------------------------------------
# Dunder = "double underscore". Special methods Python calls automatically.

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):                       # used by print()
        return f"Book: {self.title}"

    def __len__(self):                       # used by len()
        return self.pages

    def __eq__(self, other):                 # used by ==
        return self.title == other.title

b1 = Book("Python 101", 250)
b2 = Book("Python 101", 999)
print("9. Dunder methods:")
print("   str:", str(b1))
print("   len:", len(b1))
print("   eq :", b1 == b2)


# ------------------------------------------------------------
# 10. PUTTING IT TOGETHER
# ------------------------------------------------------------

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def describe(self):
        pass

class ElectricCar(Vehicle):
    def __init__(self, brand, battery_kwh):
        super().__init__(brand)
        self.battery_kwh = battery_kwh

    def describe(self):
        return f"{self.brand} EV with {self.battery_kwh} kWh battery"

print("10. Combined example:")
print("   ", ElectricCar("Tesla", 75).describe())
