a=list[input("name:"),input("name:"),input("name:")]
print(type(a),a)

soul=[]
soul1=input("name:")
soul2=input("name:")
soul3=input("name:")
soul.append(soul1)
soul.append(soul2)
soul.append(soul3)
print(soul)

so=input("name:")
soul.append(so)
so=input("name:")
soul.append(so)
print(soul)

life=[]
life.append(input("name:"))
life.append(input("name:"))
print(life)

palin=[]
palin.append(input("first:"))
palin.append(input("second:"))
palin.append(input("name:"))
copy=palin.copy()
copy.reverse()
if(copy==palin):
    print("it is palindrome")
else:
    print("it is not a palindrome")

tuppu=("C","D","A","A","B","B","A")
print(tuppu.count("A"))
tuppu=["C","D","A","A","B","B","A"]
tuppu.sort()
print(tuppu)