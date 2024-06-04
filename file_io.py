#file I/O in python for read and write data (major operation)
#text files: .txt .docx .log etc
#Binary files: ..mp4 .mov .png .jpeg etc
#we have to open file before reading or writing
#f=open("file_name","mode")
"""
basic modes
r:read mode (default)
w:write mode (overwrite)
x:create a new file and opening it for writing
a:open for writing,appending to the end of the file if it exists
b:binary mode
t:text mode
+:open a disk file for updating(reading and writing)
"""
#data=f.read() read entire line
#date=f.readline() read one line at a time
#f.close()
f=open("demo.txt","r")
data=f.read()
line1=f.readline()
print(data)
print(line1) #empty next line get printed cuz there is all data already printed
print(type(data))
f.close()
f=open("demo.txt","w")
data=f.write("this is after write file. 123")
print(data)
f.close()
f=open("demo.txt","a")
data=f.write("\nagain appending the data")
print(data)
f.close()
#r+ for reading and overwrite existing data, pointer point at start
f=open("demo.txt","r+") #overwrite the first position string
f.write("hello")
print(f.read()) #pointer shift to i so, printing from is
f.close()
#w+ for read and overwrite and truncate the file
f=open("sample.txt","w+")
f.read()
f.write("this is written after truncate")
f.close()
#a+ read and append, pointer points at the end and write
f=open("sample.txt","a+")
print(f.read()) #this is not working
f.write("this is written after appending")
f.close()