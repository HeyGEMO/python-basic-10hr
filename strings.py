str1="this is a string"
str2='string'
str3="""another string""" #for ("this one")
str4="this is string and \n this is another line string"#for next line use escape sequence characters
str5="you can use \t tab for spacing"
str6="hello"
str7="world" #adding two string i.e concatenation
str8="hellolauda"
length_of_string8=len(str8+""+str1) #spaces also count on length
print(str4)
print(str5)
print(str6+str7)
print(length_of_string8)
#indexing = positon number
str9="hello_world"
access=str9[0]
print(access,str9[4])
#slicing
#Accessing parts of a string
#str[starting_index:ending_index]
string="hello world"
print(string[1:4])
print(string[:4]) #same as 0 to 4
print(string[1:]) #same as 1 to last or use str(len)
#negative index a p p l e = -5 -4 -3 -2 -1 backward counting
print(string[-6:-1])


