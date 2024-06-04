#function and recursion
#def func_name(param1,param2...):
    #some work
    #return val
#func_name(arg1,arg2...) #function call
def calc_sum(a,b):
    sum=a+b
    print(sum)
calc_sum(2,3)
calc_sum(4,5)
def calc_sum(a,b):
    return a+b
sum=calc_sum(6,7)
print(sum)
def print_hello():
    print("hello hello")
print_hello()
def calc_avg(a,b,c):
    return (a+b+c)/3
avg=calc_avg(2,3,4)
print(avg)
#types
#built-in function
print("honey",end="") #sep = " "
print("aayo paji") #end="\n"
#user-defined function
def cal_prod(a=2,b=3):
    print(a*b)
    return a*b
cal_prod()