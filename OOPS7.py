#class method decorator
#a class method is bount to the class and recives the class as an implicit first argument.
#Note- static method cant access or modify class state and generally for utility
class student:
    name="anonymous"
    @classmethod #directly acess/change class in our function (decorator)
    def change(cls,name): #cls is reffering to the class
        cls.name=name
    #def changeName(self,name):
        #self.name=name #create new name for object but we have change class attributes
        #student.name=name #for changing the name for class attributes
        #self.__class__.name="lauda insaan" #can able to access class of object class's name changed anonymous=laudainsaan

p1=student()
#p1.changeName("akki pandy")
p1.change("aandu pandu") 
print(p1.name) #print change function
print(student.name) #anonymous= aandu pandu
