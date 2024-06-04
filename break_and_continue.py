#break
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("loop break")

#continue
i=0
while i<=10:
    if(i%2==0):
        i+=1
        continue #after this execute then line 16 and 17 wont execute it skips
    print(i)
    i+=1
