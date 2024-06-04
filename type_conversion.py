#type conversion
a=2
b=3.6
c=int("4") #type casting only work with digit not letter
sum1=a+b   #in float (add string and integer not possible)
sum2=a+c  #type conversion is automatic
print(sum1)
print(sum2,type(sum2))