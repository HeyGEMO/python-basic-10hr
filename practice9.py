def calc_natural(n):
    if(n==0):
        return 0
    return calc_natural(n-1)+n
sum=calc_natural(10)
print(sum)

list=["a","b","c","d","e"]
def print_el(list,idx=0):
    if(idx==len(list)):
        return 
    print(list[idx])
    print_el(list,idx+1)
print_el(list)