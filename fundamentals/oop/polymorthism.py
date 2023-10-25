class CoffeeM:
    def __init__(self,name):
        self.name = name
        self.water_temp = 200
    def brew_now(self,beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")
    def clean(self):
        print("Cleaning!")

class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super().brew_now(beans)
        print("Frothy!!!")
    def clean(self):
        print("Cleaning the froth!")

#overriding
class Parent:
    def method_a(self):
        print("invoking parent method_a!")
class Child(Parent):
    def method_a(self):
        print("Invoking Child method_a!")
dad = Parent()
son = Child()
dad.method_a()
son.method_a() #this overrides the parent method!
#polymorphism
# We'll use the Person class to demonstrate polymorphism
# in which multiple classes inherit from the same class but behave in different ways
class Person:
    def pay_bill(self):
        raise NotImplementedError
# Millionaire inherits from Person
class Millionaire(Person):
    def pay_bill(self):
        print("Here you go! Keep the change!")
# Grad Student also inherits from the Person class
class GradStudent(Person):
    def pay_bill(self):
        print("Can I owe you ten bucks or do the dishes?")

