#sets in python
#unique,unordered,element immutable
#list and dict cant be stored
collection={1,2,3,4,1} #ignore duplicate value
collection1=set() #empty set
print(type(collection),collection)
#set methods
collection1.add(5)
collection1.add(2)
collection1.add("ram ram")
collection.remove(1)
print(collection)
print(collection1)
collection.clear() #clear the set
print(collection)
collection={"ram ram","narayan","prabhu","krishn",1}
print(collection.pop()) #generate random elements
print(collection.union(collection1))
print(collection.intersection(collection1))
