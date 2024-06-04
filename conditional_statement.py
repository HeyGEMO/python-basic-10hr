"""
1) if-elif-else
if(condition1):
    Statement1  //written after 4 spaces level
elif(condition2):
    Statement2
else:
    Statement N
"""
#traffic light code
"""
light=input("color:")
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look out")
else:
    print("light is broken")
"""
#grades of students
"""
marks=int(input("marks: "))
if(marks>=90):
    print("A")
elif( marks>=80 and marks<90):
    print("B")
elif( marks>=70 and marks<80 ):
    print("C")
else:
    print("D")
"""
#if-elif
#if
#nesting
#if(condition)
#    if(condition2)
#        statement

age=34
if(age>=18):
    if(age>=80):
        print("can not drive")
    else:
        print("can drive")
else:
    print("cannot drive")