#Single line If/Ternary operator
#<var>=<val1>if<condition>else<val2>
"""
food=input("food:")
eat="yes" if food == "cake" else "no"
print(eat)
"""
#<stt1>if<condition>else<stt2>
"""
food=input("food:")
print("sweet") if food=="cake" or food=="jalebi" else print("non sweet")
"""
#Cleaver if/ Ternary operator
#<var>=(false_val,true_val)[<condition>]
"""
age=int(input("age:"))
vote=("yes","no")[age<=18]
print("age",age,"can vote ??",vote)
"""
# sal=float(input("salary is:")) select then ctrl+forward slash (/)
# tax=sal*(0.1,0.2)[sal>=50000]
# print(tax)