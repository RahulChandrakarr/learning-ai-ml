class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

    def have_birthday(self):
        self.age = self.age + 1
        print(f"{self.name} is now {self.age}.")


dog1 = Dog("doggi", 4)

dog1.bark()
dog1.describe()
dog1.have_birthday()
dog1.describe()
