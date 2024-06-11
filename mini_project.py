#random password generator
import random
import string #collection of string constant
pass_len=12
charValues=string.ascii_letters+string.digits+string.punctuation
password = ""
for i in range(pass_len):
    password+=random.choice(charValues)
print("your generated password is:",password)
#random.choice([1,2,3]) #generate random from the list

#alternative method ( list comprehension)
result=[random.choice(charValues) for i in range(pass_len)]
print(result)
result="X".join([random.choice(charValues) for i in range(pass_len)])
print(result)
result="".join([random.choice(charValues) for i in range(pass_len)])
print(result)