#with syntax
#with open("demo.txt","a")as f:
    #data=f.read()
with open("sample.txt","r") as f: #as=alias
    data=f.read()
    print(data)

with open("sample.txt","w") as f:
    data=f.write("this is new data")

#deleting a file
#we have to use module
import os #it is pre installed moduled
#pip is package installer in python /pip3
os.remove("example.txt") #for file delete 