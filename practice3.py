num1=int(input("enter the number:"))
if(num1%2==0):
    print("it is even number")
else:
    print("it is odd number")
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
if(num1>num2 and num1>num3):
    print(num1,"is greater")
elif(num2>num3):
    print(num2,"is greater")
else:
    print(num3,"is greater")
if(num1%7==0):
    print(num1,"is multiple of 7")
else:
    print(num1,"is not multiple of 7")