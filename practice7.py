numbers=[1,4,9,16,25,36,49,64,81,100]
tup=(1,4,9,16,25,36,49,64,81,100)
"""
for value in numbers:
    print(value)
"""
"""
x=36
i=0
for num in tup:
    if(num==x):
        print(x,"is found at index:",i)
        break
    print(num)
    i+=1
"""
"""
for val in range(100,1,-1):
    print(val)
"""
"""
n=int(input("enter the n number:"))
for multi in range(n,(n*10)+n,n):
    print(multi)
print("end of loop")
#alternaties
for multiple in range(1,11):
    print(n*multiple)
print("end of loop")
"""
number=int(input("enter the nth number:"))
i=1
sum=0
while i<=number:
    i+=1
    sum+=i
print(sum)
factorial=number
for val in range(1,number):
    factorial=val*factorial
print(factorial)