#inheritance
#when one class(child/derived) derives the properties and methods of another class(present/base)
"""
class car:
    color="black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class toyotaCar(car):
    def __init__(self,name) -> None:
        self.name=name
    
car1=toyotaCar("fortuner")
car2=toyotaCar("prius")

print(car1.start())
print(car1.color)
"""
#types
#1) single inheritance=single parent/base class and single child class
#2)multi-level inheritance=parent class => derived class => derived class
class car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class toyotaCar(car):
    def __init__(self,brand) -> None:
        self.brand=brand
    
class fortuner(toyotaCar):
    def __init__(self,type) -> None:
        self.type=type

car1=fortuner("diesel")
car1.start()
print(car1.type)
#3)Multiple inheritance= derived class can inherit multiple base classes's properties
class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class C(A,B):
    varC="welcome to class C"
c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)


