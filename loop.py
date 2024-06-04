#loops in python
#while loop
#while condition:
    #some work
count=1
while count<=5: #iteration process
    print("hello")
    count=count+1 #count+=1

#for loops
list=[1,2,3,4,5,6,7,8,9,0]
tup=(2,4,6,2,7,8)
for el in list: #el is variable all element stored in el
    print(el)
for val in tup: #traverse
    print(val)
#for loops with else
str="yo yo honey singh"
for char in str:
    if(char=="h"):
        print("h found")
        break
    print(char)
else:
    print("end")

#range() return sequence start from 0 and increment by 1
#range(start?,stop,step?)
seq=range(5) #0 to n-1
for i in seq:
    print(i)
print("end of loop")
for n in range(1,20,4):
    print(n)

#pass statement: it is a null statement
for i in range(5):
    pass #skip loop:used for future code