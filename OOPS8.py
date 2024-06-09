#@property decorator
#we use @property decorator on any method in the class to use the method  as a property
class student:
    def __init__(self,phy,che,math) -> None:
        self.phy=phy
        self.che=che
        self.math=math
        
        #self.percentage=str((self.phy+self.che+self.math)/3)+"%"

        #manual method for changing attribute value
    #def changePer(self):
        #self.percentage=str((self.phy+self.che+self.math)/3)+"%"

        #alternative
    @property
    def percentage(self):
        return str((self.phy+self.che+self.math)/3)+"%" #latest calculated value return

stu1=student(98,88,99) 
print(stu1.percentage) #for line 9 #percentage value set as old value even we change the marks its print old percentage
#when we can not give fixed value for the attribute then we use property
#attribute value depend upon function then we can make function a property
#stu1.phy=78 # for line 10 11 12
#stu1.changePer() #for line 10 11 12
#print(stu1.percentage) #for line 10 11 12
stu1.phy=67
print(stu1.percentage)
#decorator=getter and setter for explore more