def check_for_word():
    word="learning"
    with open("practice.txt","r") as f:
#with open("practice.txt","w") as f:
    #f.write("hi everyone\nwe are learning File I/O\n")
    #f.write("using java\ni like programming in java")
        data=f.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")
    new_data=data.replace("java","python")
    print(new_data)

    with open("practice.txt","w") as f:
        f.write(new_data)
check_for_word()
def check_for_line():
    word="learning"
    data=True
    Line_no=1
    with open("practice.txt") as f:
        while data:
            data=f.readline() #reading line
            if(word in data): #checking if word exists in data
                print(Line_no)
            Line_no+=1
    return -1
check_for_line()
with open("example2.txt","r") as f:
    data=f.read()
    print(data)
#primitive
"""
    num="" #empty variable
    for i in range(len(data)): #loop from 0th index to last index
        if(data[i]==","): #if comma encounter means print number 
            print(num)
            num=""  #make empty again
        else:
            num+=data[i] #if comma not encounter then add the index and increment to next index
"""
#alternative
count=0
nums=data.split(",") #creating list
for val in nums: #checking the list
    if(int(val)%2==0): #checking if it is even number
        count+=1
print(count) #total number of even number