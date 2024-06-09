#polymorphism : eg. operator overloading
#when the same eoperator is allowed to have different meaning according to the context.
#operators and dunder functions
"""
a+b #addition a.__add__(b)
a-b #subtraction a.__sub__(b)
a*b #multiplication a.__mul__(b)
a/b #division a.__div__(b)
a%b #addition a.__mod__(b)
"""
#basic examples of implicit overloading
print(1+3) #4
print("allu"+"arjun") #concatenate strings
print([1,2,3]+[4,5,6]) #merge list