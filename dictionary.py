#dictionary in python which is builtin function
#mutable,unordered,dont allowed duplicate keys
#"key":value
info={
    "name" : "akku",
    "cgpa" : 3.2,
    "marks" : [99,97,98],
    "is_adult" : True,
}
null_dict={    }
info["name"]="cheu"
info["surname"]="chaudhary"
print(type(info),info)
print(info["name"])

#nested dictionaries
student={
    "name":"lauda kumar",
    "subject":{
        "phy":78,
        "chem":88,
        "math":99,
    }
}
print(student["subject"])
print(student.keys()) #all dictionaries keys
print(list(student.keys()))
print(len(list(student.keys())))
print(student.values()) #all values
print(student.items()) #all pairs as tuple
pairs=list(student.items())
print(pairs[0])
print(info.get("cgpa")) #return value of key
print(info["cgpa"])
#print(info["cgpa2"]) return error
info.update(student) #update dictionaries double key and value will be overwrite
print(info)