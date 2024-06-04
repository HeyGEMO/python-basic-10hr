#list is built data types
marks=[94.4,95.2,66.4,45.1] #list
student=["karuna",15,"change"] #sorting works on string too
student[0]="chetana"
print(marks)
print(marks[0],marks[3])
print(len(marks))
print(student)
#slicing possible same as list slicing
print(marks[1:3])
#List methods (function)
student.append("ashika") #mutation
marks.sort() #sort in ascending
print(student)
print(marks)
marks.sort(reverse=True) #sort in descending order
print(marks)
student.reverse() #reverse list
print(student)
student.insert(2,"diksha") #to insert in index
print(student)
student.remove("change") #to remove first occurance of element not working
print(student)
student.pop(2) #remove element at index
