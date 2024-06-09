#static method
#no self parameter used (works at class level)
#special type method
class student:
    @staticmethod #decorator
    def college():
        print("everest lauda college")
    college()

#abstraction
#hiding the implementation details of a class and only showing the essential features to the user.
class car:
    def __init__(self) -> None:
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("car started")
car1=car()
car1.start() #doesnot print unnecessary details only shows necessary output

#encapsulation
#wrapping data and functions into a single unit(object).