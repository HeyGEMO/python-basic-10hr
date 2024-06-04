#recursion function
cities=["bhaktapur","palpa","butwal","kathmandu","bhairahawa","lalitpur"]
heros=["thor","iron man","deadpool","hulk","captain america","dr. strange","spoodermon"]
def print_length(List):
    print(len(List))
def print_list(List):
    for item in List:
        print(item,end=" ")

def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)

def currency(n):
    usd=131.6
    print(n/usd,"$")
def number_checker(n):
    if(n%2==0):
        print(n,"is even")
    else:
        print(n,"is odd")
print_length(cities)
print_length(heros)
print_list(heros)
calc_fact(5)
nepalese=int(input("enter the nepalese currency:"))
currency(nepalese)
number=int(input("enter the number:"))
number_checker(number)
