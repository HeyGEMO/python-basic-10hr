dict={
    "table":["a piece of furniture","list of facts and figures"],
    "cat":"a small animal",
}
print(dict)
subject={"python","java","c++","python","javascript","java","python","java","c++","c"}
print("classroom needed for each subject:",len(subject))

marks={}
x=int(input("enter phy marks:"))
marks.update({"phy":x})
x=int(input("enter che marks:"))
marks.update({"che":x})
x=int(input("enter math marks:"))
marks.update({"math":x})
print(marks)

values={9,9.0,9.25,"9.0"}
print(values)
values2={
    ("int",9),
    ("float",9.0)
    }
print(values2)
