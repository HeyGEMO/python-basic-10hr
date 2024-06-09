#super method
#super() method is used to access methods of the parent class for inherit
class car:
    def __init__(self,type) -> None:
        self.type=type
    
    @staticmethod #static method decorator
    def start():
        print("car is started")
    @staticmethod #common for all object in this class
    def stop():
        print("car is stopped")
    
class toyotaCar(car):
    def __init__(self,name,type) -> None:
        super().__init__(type) #passing type on constructor
        self.name=name
        super().start() #using this parent method is called
        #self.type=type #type created inside the toyota but we need to change type from parent class not in child 

car1=toyotaCar("fortuner","petrol")
#print(car1.type) #cant call direct parent ("type") so we use super
print(car1.type)


        
