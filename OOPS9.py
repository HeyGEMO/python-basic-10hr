#polymorphism : eg. operator overloading
#when the same eoperator is allowed to have different meaning according to the context.
#operators and dunder functions (double underscore __)
"""
a+b #addition a.__add__(b)
a-b #subtraction a.__sub__(b)
a*b #multiplication a.__mul__(b)
a/b #division a.__div__(b)
a%b #addition a.__mod__(b)
"""
#examples of implicit overloading
print(1+3) #4
print("allu"+"arjun") #concatenate strings
print([1,2,3]+[4,5,6]) #merge list
#examples of explicit overloading
class complex:
    def __init__(self,real,imag) -> None:
        self.real=real
        self.imag=imag
    
    def showNumber(self):
        print(self.real,"i+",self.imag,"j")
    
    #function for adding two complex number (manual method)
    """
    def add(self,num2):
        newReal=self.real+num2.real
        newImag=self.imag+num2.imag
        return complex(newReal,newImag)
        """
    #using dunder function
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImag=self.imag+num2.imag
        return complex(newReal,newImag)
    
    def __sub__(self,num2):
        newReal=self.real-num2.real
        newImag=self.imag-num2.imag
        return complex(newReal,newImag)

num1=complex(1,3)
num1.showNumber()

num2=complex(4,5)
num2.showNumber()

#num3=num1.add(num2) for manual method
num3=num1 + num2
num3.showNumber()
num3=num1-num2
num3.showNumber()