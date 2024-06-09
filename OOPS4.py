#del keyword
#used to delete object properties or object itself
#del s1.name
#del s1
"""
class student:
    def __init__(self,name) -> None:
        self.name=name

s1=student("akku")
print(s1.name) #public key
del s1.name
print(s1.name)
"""
#private(like) attribute or method
#private atrributes and methods are meant to be used only within the class and are not accessible from outside the class

class account:
    __name="anonymous"
    def __init__(self,acc_no,acc_pass) -> None:
        self.acc_no=acc_no
        self.__acc_pass=acc_pass #private __

    def reset_pass(self):
        print(self.__acc_pass) #working here cuz inside the class

    def __hello(self): #we can make function private too
        print("hello world")
    
    def welcome(self):
        self.__hello()

acc1=account("akky","lauda123")
print(acc1.acc_no)
print(acc1.reset_pass())
acc2=account()
print(acc2.welcome())
print(acc1.__acc_pass) #not working cuz outside the class


