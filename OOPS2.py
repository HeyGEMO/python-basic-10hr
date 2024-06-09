#class and instance attributes
#class.attr=common for all objects, stores only one time in the memory
#obj.attr=different for all objects
#student(class) = s1,s2,s3,s4
#eg:
class student:
    college_name="everest" #class attributes
    name="anonymous" #used for by defualt
    def __init__(self,name,marks): #constructor for object initialization (parametrize constructor)
        self.name=name
        self.marks=marks

    def welcome(self): #method
        print("welcome student",self.name)
    def get_marks(self):
        return self.marks
#methods
#class have data and methods stored
#attributes = properties
#methods = what it can do
#methods are basically a functions that belongs to object
s1=student("akku pandy",101)
s1.welcome()
print(s1.get_marks())
