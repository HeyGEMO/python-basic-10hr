#recursion function
#call itself
"""
def show(n):
    if(n==0): #base case=stop or not
        return
    print(n)
    show(n-1)
    print("end") #look what happens due to call stack system 
show(5)
"""
def fact(n):
    if(n==0 or n==1):
        return 1 #return to previous layer
    else:
        return n*fact(n-1)
print(fact(5))