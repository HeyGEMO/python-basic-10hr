#OOPS in python
#class=blueprint
"""
#creating class
class student: #blue print
    name="lauda lassan" #properties
#creating object(instance)
s1=student() #s1 is object
print(s1.name) #calling object
"""
class car:
    car_name="thar"
    color="black"
    brand="mahendra"
car1=car()
print(car1.color)
print(car1.brand)

#constructor: it is __init__ function (specital function which invoke at the time of object creation)
#all classes have function which is always executed when the class is initiated
#init always execute there is built in constructor
#but we can create manually for desired feature
class student:
    def __init__(self,name,marks): #self means new object created is self object
        print(self) #check what is self
        self.name=name #self.name is instance attributes which is different for all object
        self.marks=marks
        print("adding new student in database") #always self argument should pass on constructor
        
s1=student("lauda insaan",98) #we can write self to anyname
print(s1.name,s1.marks)

s2=student("lando army",55) #constructor call here
print(s2.name,s2.marks) #parameter should be matched

